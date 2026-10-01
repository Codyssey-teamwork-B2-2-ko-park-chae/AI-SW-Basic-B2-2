# 🛠️ Git Troubleshooting Log (트러블슈팅 실습 및 증빙 기록)

이 문서는 협업 중 발생할 수 있는 주요 Git 문제 상황 4가지에 관한 기존 기록과 재현 결과를 정리합니다. 원본 터미널 로그가 확인되지 않는 작업은 실제 수행 증빙으로 단정하지 않고, 원격 커밋과 로컬 재현을 구분합니다.

**문서 점검 기준: 2026-10-01 (한국 시간).** 현재 구현 경로는 `src/utils/`입니다. 아래 독립 클론 로그는 과거 커밋·브랜치를 대상으로 남긴 기존 재현 기록이며, 이번 문서 점검에서 다시 수행한 로그가 아닙니다. 따라서 로그의 `src/math_ops.py`, `src/date_ops.py` 등 과거 경로를 그대로 유지합니다. 최신 테스트 환경은 [가상환경 가이드](command/python_venv_pytest.md), 제출 증빙은 [제출 인덱스](../SUBMISSION.md)를 참고합니다.

---

## 시나리오 1: `git commit --amend` (최근 커밋 수정 및 완성도 향상)

### 👥 참여자
- **실행자:** 고준석 (`kjs83036`)
- **검토자:** 채민성 (`CMS-SUDO7`)

### 📌 상황 (Situation)
- 기존 기록에는 `src/utils/math_ops.py` 작업 후 amend를 수행했다고 적혀 있으나 원본 터미널 로그와 reflog가 없어 당시 실행 여부는 확인되지 않습니다.
- 이 시나리오의 목적은 amend 동작을 설명하는 것이며, 원격 커밋 `cbdf63c`는 해당 실습 결과가 아닙니다.

### 🛠️ 절차 예시 (원본 수행 로그 아님)
```bash
# 1. 파일 수정: power 함수에 타입 어노테이션 및 docstring 보완
# 2. 수정한 파일 스테이징
git add src/utils/math_ops.py

# 3. 기존 커밋에 수정사항을 흡수시키며 커밋 메시지도 명확하게 갱신
git commit --amend -m "feat: 거듭제곱 함수 타입 힌트와 설명 보완"

# 4. 히스토리 검증
git log -n 1
```

### 🔎 원본 실행 증빙 확인 결과
기존 제출본에 기재된 터미널 출력은 검증 가능한 원본 로그나 reflog와 대조할 수 없어 실제 세션 증빙으로 사용하지 않습니다. 출력에 적힌 `a1b2c3d`는 원격 커밋에서 확인되지 않습니다. `cbdf63c`는 원격에 존재하지만 실제 제목은 `feat: add power and add  function with type annotations and docstring`이고 `src/math_ops.py`의 과거 커밋입니다. 따라서 아래 amend 세션의 결과 해시·메시지로 볼 수 없습니다.

### 🎯 결과 및 주의점 (Outcome & Caveats)
- 원본 로컬 `reflog`를 확보하지 못했으므로 이 amend 실습이 수행되었는지, 어떤 해시가 생성되었는지, 푸시되었는지는 확인할 수 없습니다.
- **주의점:** 이미 `origin`에 push된 커밋을 amend하면 새 커밋이 만들어져 원격과 로컬의 히스토리가 달라질 수 있습니다. 협업 브랜치에서는 팀 합의 없이 강제 푸시하지 말고, amend는 미푸시 커밋을 정리할 때 사용합니다.

### 💡 왜 이 방법을 선택했는가 (Why)
- `amend`는 미푸시 커밋의 변경 내용이나 메시지를 정리할 때 사용할 수 있습니다.

#### 재현 실행 기록 (독립 클론)
```text
$ git clone --no-hardlinks --no-checkout <로컬 저장소> /tmp/troubleshooting-repro-s1
$ git -C /tmp/troubleshooting-repro-s1 checkout --detach cbdf63c
HEAD is now at cbdf63c feat: add power and add  function with type annotations and docstring
$ git -C /tmp/troubleshooting-repro-s1 commit --amend -m "feat: add power and add  function with type annotations and docstring"
[detached HEAD b6480ef] feat: add power and add  function with type annotations and docstring
 2 files changed, 10 insertions(+)
```
재현에서는 사전 커밋의 작업 트리가 아니라 기존 원격 기능 커밋 `cbdf63c`를 체크아웃해 amend 동작만 확인했습니다. 생성된 `b6480ef`는 재현 환경의 로컬 커밋으로 원격에 푸시되지 않았습니다. 해당 커밋에 있는 파일 경로는 `src/math_ops.py`입니다. 따라서 이 재현은 원래 파일 편집부터 amend까지의 전체 세션이나 원본 수행 사실을 입증하지 않습니다.

---

## 시나리오 2: `git reset --soft HEAD~1` (로컬 커밋 취소 및 작업 보존)

### 👥 참여자
- **실행자:** 채민성 (`CMS-SUDO7`)
- **검토자:** 박영세 (`MetaStudy999`)

### 📌 상황 (Situation)
- 기존 기록은 문자열 유틸 코드와 임시 노트를 한 커밋에 포함한 뒤 reset했다고 서술하지만, 그 시작 커밋 `9f8e7d6`이 저장소에서 확인되지 않고 원본 터미널 로그도 없습니다.
- 따라서 이 상황 설명은 검증된 사건 기록이 아니라 soft reset 절차를 설명하기 위한 시나리오입니다. 아래 별도 재현은 이 절차만 다시 확인한 것입니다.

### 🛠️ 절차 예시 (원본 수행 로그 아님)
```bash
# 1. 변경사항을 Staging Area에 그대로 보존한 채 커밋만 직전 상태로 취소
git reset --soft HEAD~1

# 2. 스테이징 영역 상태 확인
git status

# 3. 임시 문서는 Staging Area에서 제외(Unstage) 및 정리
git restore --staged docs/temp_notes.md
rm docs/temp_notes.md

# 4. 기능 코드만 온전히 스테이징하여 단일 책임 커밋 생성
git add src/utils/string_ops.py
git commit -m "feat: add slugify and truncate_words utilities"
```

### 🔎 원본 실행 증빙 확인 결과
기존 제출본의 출력에는 시작 커밋 `9f8e7d6`이 적혀 있으나 저장소에서 확인되지 않습니다. 실제 원본 실행 로그가 없으므로 이 출력을 수행 증빙으로 사용할 수 없습니다. `08da39a`는 원격에 존재하는 기능 커밋이지만, 해당 reset 세션의 마지막 출력이라고 입증되지는 않았습니다.

### 🎯 결과 및 주의점 (Outcome & Caveats)
- 원본 실행 증빙이 없어 이 실습에서 코드가 보존되었는지, `08da39a`가 그 결과였는지는 확인할 수 없습니다.
- 원격 기록에서 `08da39a`의 존재와 PR #19 병합은 확인되지만, 이는 실습을 수행했다는 증거가 아닙니다.
- **주의점:** `reset --mixed`는 인덱스(Staging Area)까지 언스테이징하고, `reset --hard`는 작업 트리의 변경사항까지 영구 삭제하므로 커밋 재구성 시에는 가장 안전한 `--soft` 옵션을 사용하는 것이 필수적입니다.

### 💡 왜 이 방법을 선택했는가 (Why)
- `git reset --soft`는 HEAD 포인터만 이전 커밋으로 되돌리고 스테이징 영역과 작업 트리의 내용을 100% 안전하게 살려두므로, 잘못 묶인 커밋을 쪼개거나 메시지를 대폭 재작성할 때 가장 안전하고 적합한 방법이기 때문입니다.

#### 재현 실행 기록 (독립 클론)
저장소에 기록된 시작 커밋 `9f8e7d6`은 존재하지 않아, 실제 브랜치 `feature/chae-advanced-strings`의 HEAD `8c0c9cd`에서 동일한 혼합 커밋 → soft reset → 노트 언스테이지 및 삭제 → 기능 코드만 커밋하는 흐름을 재현했습니다. 해당 브랜치는 경로 리팩터링이 반영되어 실제 기능 파일은 `src/utils/string_ops.py`입니다. 재현용으로 `truncate_chars` 함수와 임시 노트를 만들었습니다.

```text
$ git clone --no-hardlinks --no-checkout "$(git rev-parse --show-toplevel)" /tmp/troubleshooting-s2-faithful
$ git -C /tmp/troubleshooting-s2-faithful fetch origin refs/remotes/origin/feature/chae-advanced-strings:refs/remotes/origin/feature/chae-advanced-strings
$ git -C /tmp/troubleshooting-s2-faithful checkout -B feature/chae-advanced-strings origin/feature/chae-advanced-strings
Switched to a new branch 'feature/chae-advanced-strings'
$ git -C /tmp/troubleshooting-s2-faithful log -1 --oneline
8c0c9cd Merge branch 'main' into feature/chae-advanced-strings
$ cd /tmp/troubleshooting-s2-faithful
$ git config user.name 'CMS_SUDO7'
$ git config user.email 'cms-sudo7@example.invalid'
$ cat >> src/utils/string_ops.py <<'EOF'


def truncate_chars(text: str, max_chars: int, suffix: str = "...") -> str:
    """Limit a string to max_chars characters, adding a suffix when shortened."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + suffix
EOF
$ cat > docs/temp_notes.md <<'EOF'
# Temporary notes

Review the new string helper before splitting this mixed commit.
EOF
$ git add src/utils/string_ops.py docs/temp_notes.md
$ git commit -m 'feat: add string helper and update docs'
[feature/chae-advanced-strings 8274958] feat: add string helper and update docs
 2 files changed, 10 insertions(+)
 create mode 100644 docs/temp_notes.md
$ git log -n 1 --oneline
8274958 feat: add string helper and update docs
$ git reset --soft HEAD~1
$ git status
On branch feature/chae-advanced-strings
Your branch is up to date with 'origin/feature/chae-advanced-strings'.
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   docs/temp_notes.md
	modified:   src/utils/string_ops.py
$ git restore --staged docs/temp_notes.md
$ rm docs/temp_notes.md
$ git add src/utils/string_ops.py
$ git commit -m 'feat: add truncate_chars utility'
[feature/chae-advanced-strings b67b0ba] feat: add truncate_chars utility
 1 file changed, 7 insertions(+)
$ git log -n 1 --oneline
b67b0ba feat: add truncate_chars utility
$ git status --short --branch
## feature/chae-advanced-strings...origin/feature/chae-advanced-strings [ahead 1]
```

**결과:** staged source change와 staged note가 soft reset 뒤 모두 남았고, 노트만 unstage 후 삭제하여 기능 파일만 커밋됐습니다. 재현용 커밋은 원격에 push하지 않았습니다. 이 검증은 실제 브랜치 HEAD에서 증빙과 같은 절차를 재현한 것이며, 존재하지 않는 `9f8e7d6`의 원래 혼합 변경 상태를 재현한 것은 아닙니다. `08da39a`는 저장소에 존재하는 기능 커밋이지만, 그 부모에는 임시 노트가 없어 기록된 시작 상태와는 다릅니다. 또한 브랜치의 실제 파일 경로가 `src/utils/string_ops.py`여서 해당 경로를 사용했습니다.

---

## 시나리오 3: `git revert` (원격에 push된 커밋의 안전한 취소)

### 👥 참여자
- **실행자:** 박영세 (`MetaStudy999`)
- **검토자:** 고준석 (`kjs83036`)

### 📌 상황 (원격 기록에서 확인되는 사실)
- 원격 이력에는 주석 추가 커밋 `b9c1222`와 그 변경을 되돌리는 커밋 `ebce9a2`가 존재합니다. 로컬 터미널 원본이 없어 당시 실행 명령과 push 작업 자체는 원격 이력만으로 확인할 수 없습니다.

### 🛠️ 절차 예시 (원본 수행 로그 아님)
```bash
# 1. 취소 대상 커밋 해시 확인
git log --oneline -n 2

# 2. 해당 커밋의 변경사항을 정반대로 상쇄하는 신규 역방향 커밋 생성
git revert b9c1222 --no-edit

# 3. 히스토리 검증
git log -n 2

# 4. 원격 저장소로 안전하게 push
git push origin feature/park-date-utils
```

### 🔎 원격 커밋 객체 확인
```text
ebce9a2595e7073e8a4f1bd92ee68c6657fe1f60 Revert "docs: add comment to date operations"
Author/Commit date: Tue Sep 15 16:56:30 2026 +0900
src/date_ops.py | 3 deletions(-)
```

### 🎯 결과 및 주의점 (Outcome & Caveats)
- 원격 Git 이력에는 `ebce9a2`가 실제 revert 커밋으로 존재하고 PR #16의 병합 이력에 포함됩니다. 커밋 객체의 변경 요약은 세 줄 삭제이며 날짜는 `16:56:30 +0900`입니다.
- 기존 제출본의 터미널 출력에 적힌 날짜 `17:42:10`과 변경량 `1 deletion`은 커밋 객체와 일치하지 않아 제거했습니다. 실제 `git revert` 명령 실행 및 push 세션은 원본 터미널 자료가 없어 확인 불가입니다.

### 💡 왜 이 방법을 선택했는가 (Why)
- 원격 저장소에 공유된 커밋을 되돌릴 때는 기존 히스토리를 삭제(rewrite)하지 않고 "취소되었다"는 사실 자체를 새로운 커밋으로 명시하는 `revert`가 협업의 황금률(Golden Rule)이기 때문입니다.

#### 재현 실행 기록 (독립 클론)
```text
$ git clone --no-hardlinks --no-checkout <로컬 저장소> /tmp/troubleshooting-repro-s3
$ git -C /tmp/troubleshooting-repro-s3 checkout --detach b9c1222
$ git -C /tmp/troubleshooting-repro-s3 revert b9c1222 --no-edit
[detached HEAD e9e8bed] Revert "docs: add comment to date operations"
 1 file changed, 3 deletions(-)
$ git -C /tmp/troubleshooting-repro-s3 log -2 --oneline
e9e8bed Revert "docs: add comment to date operations"
b9c1222 docs: add comment to date operations
```
revert는 성공했습니다. 새 해시(`e9e8bed`)는 재현 시각과 커미터 정보가 달라 기존 로그의 `ebce9a2`와 다릅니다. 원격 저장소 변경은 하지 않았으므로 push 결과는 재현하지 않았습니다.

---

## 시나리오 4: `git stash` & `git stash pop` (작업 임시 보관 및 Context 전환)

### 👥 참여자
- **실행자:** 박영세 (`MetaStudy999`) / 고준석 (`kjs83036`)
- **검토자:** 팀 전원

### 📌 상황 (기존 기록의 설명, 원본 자료 미확인)
- 기존 문서는 `feature/park-date-utils`에서 미완성 상대 시간 계산 코드를 stash하고 `main` 점검 후 복원했다고 서술합니다. 당시 작업 트리와 stash를 확인할 원본 터미널 기록은 확보되지 않았습니다.

### 🛠️ 절차 예시 (원본 수행 로그 아님)
```bash
# 1. 현재 작업 중인 수정사항을 Stash 스택에 안전하게 보관
git stash push -m "WIP: date utils relative time"

# 2. 작업 트리가 깨끗해진 상태(Clean Working Tree) 확인
git status

# 3. main 브랜치로 전환하여 요청받은 점검 수행
git checkout main
# (main 브랜치에서 단위 테스트 및 PR 상태 점검 완료)

# 4. 다시 작업 브랜치로 복귀
git checkout feature/park-date-utils

# 5. Stash 스택에 저장해 두었던 작업 내용을 복원하고 스택에서 제거
git stash pop

# 6. 작업 복원 확인 후 개발 재개
git status
```

### 🔎 원본 실행 증빙 확인 결과
기존 제출본의 stash 출력은 원본 터미널 세션과 대조할 수 없어 실제 수행 증빙으로 사용하지 않습니다. 특히 `d7b8e9f1a2c3...`는 끝까지 확인된 stash 객체 ID가 아니므로 증거 해시로 인용하지 않습니다. 아래 독립 클론 기록은 stash/pop 절차의 별도 재현이며 원래 작업 내용이나 수행자를 입증하지 않습니다.

### 🎯 결과 및 이점 (Outcome & Benefits)
- 독립 클론에서 WIP 한 줄을 stash/pop하는 절차는 재현했습니다. 당시 원래 작업 트리가 무손실 복원됐는지는 확인할 수 없습니다.
- `6404b67`은 원격의 문서 커밋이며 PR #16 이력에 포함됩니다. stash 이후 작업 내용을 이 커밋으로 저장했다는 사실은 이 커밋만으로 입증되지 않습니다.

### 💡 왜 이 방법을 선택했는가 (Why)
- 작업을 포기하거나 불완전한 임시 커밋을 남기지 않고도 작업 트리를 즉시 깨끗하게 비워 안전한 브랜치 체크아웃을 보장하는 Git 고유의 최적 메커니즘이기 때문입니다.

#### 재현 실행 기록 (독립 클론)
```text
$ git clone --no-hardlinks --no-checkout <로컬 저장소> /tmp/troubleshooting-repro-s4
$ git -C /tmp/troubleshooting-repro-s4 fetch <로컬 저장소> refs/remotes/origin/feature/park-date-utils:refs/remotes/origin/feature/park-date-utils
$ git -C /tmp/troubleshooting-repro-s4 checkout -B feature/park-date-utils origin/feature/park-date-utils
Switched to a new branch 'feature/park-date-utils'
$ # src/date_ops.py에 임시 WIP 한 줄 추가
$ git stash push -m "WIP: date utils relative time"
Saved working directory and index state On feature/park-date-utils: WIP: date utils relative time
$ git status --short
$ git checkout main
Switched to branch 'main'
$ git checkout feature/park-date-utils
Switched to branch 'feature/park-date-utils'
$ git stash pop
Changes not staged for commit:
  modified:   src/date_ops.py
Dropped refs/stash@{0}
$ git status --short --branch
## feature/park-date-utils...origin/feature/park-date-utils
 M src/date_ops.py
```
stash/pop 동작은 로그에 적힌 브랜치와 파일에서 성공했습니다. 다만 기존 기록의 diff 내용과 당시 변경 상태는 확보하지 못해 재현용 주석 한 줄을 사용했습니다. 따라서 stash 절차는 재현됐지만 수행자의 원래 미완성 변경 내용까지 재현됐다고 볼 수는 없습니다.

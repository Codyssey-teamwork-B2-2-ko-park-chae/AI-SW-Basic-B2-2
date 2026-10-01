# 💥 Conflict Resolution Log (충돌 해결 기록)

우리 팀(고준석, 박영세, 채민성)이 Git 협업 과정에서 마주친 충돌 상황과 이를 해결한 절차 및 학습 내용을 실제 저장소 히스토리에 기반하여 기록합니다.

**점검 기준: 2026-10-01 (한국 시간).** 원격 PR #28의 병합과 최종 정책을 재확인했습니다. 현재 로컬 브랜치는 `ko-string-policy-tabs`(HEAD `9547205`)로, `utils/string-policy.md`의 문구는 스페이스·탭 제거입니다. 아래 PR #28의 스페이스·탭·줄바꿈 제거 결과는 원격 `main`을 기준으로 합니다.

---

## 충돌 기록 #1: `src/__init__.py` 모듈 Export 통합 (내용 충돌 기록)

### 참여자 및 확인 근거

- **작업 브랜치·PR 작성자:** 채민성, `feature/chae-string-utils`, [PR #3](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/3).
- **수학 모듈 작업자:** 고준석.
- **해결 커밋 작성자:** `2847fe1`의 Git author는 `jun_seok_ko`입니다. PR 작성자와 커밋 작성자를 구분합니다.

기존 문서는 같은 export 영역을 양쪽에서 수정한 Hunk 충돌로 설명합니다. 로컬 Git 객체에서 병합 커밋 `2847fe1`과 두 부모(`7f70335`, `8adbd3d`), 최종 export 통합은 확인했습니다. 당시 터미널 로그나 충돌 마커 원본은 없어 실제 충돌 화면과 실행 명령은 확정하지 않습니다.

### 양쪽 변경과 최종 코드

첫 번째 부모 `7f70335`의 `src/__init__.py`는 문자열 함수 세 개만 export합니다. 두 번째 부모 `8adbd3d`에는 수학 함수 여섯 개(`calculate_average` 포함)가 있습니다. 병합 결과는 양쪽 공개 함수를 모두 남기는 형태입니다.

**커밋 `2847fe1`의 실제 파일 내용:**

```python
from src.string_ops import capitalize_words, reverse_string, strip_all_whitespace
from src.utils.math_ops import add, calculate_average, divide, multiply, power, subtract
__all__ = ["capitalize_words", "reverse_string", "strip_all_whitespace", "add", "subtract", "multiply", "divide", "power", "calculate_average"]
```

이 내용은 과거 커밋을 그대로 보여줍니다. 당시 수학 파일은 `src/math_ops.py`였으므로 위 `src.utils.math_ops` import에는 경로 불일치가 있습니다. export 이름 통합과 실행 가능한 import 경로 검증은 별개이며, 이 커밋만으로 정상 import 또는 테스트 통과를 단정하지 않습니다. 현재 통합 진입점은 `src/utils/__init__.py`이며 상대 import를 사용합니다.

### 이력 확인 방법

다음은 저장소 루트에서 실행하는 읽기 전용 확인 명령이며, 당시 수행 로그를 대체하지 않습니다.

```bash
git show --no-patch --format=fuller 2847fe1
git show 2847fe1^1:src/__init__.py
git show 2847fe1^2:src/__init__.py
git show 2847fe1:src/__init__.py
```

- **해결 병합 커밋:** `2847fe1` (`Merge branch 'main' into feature/chae-string-utils`).
- **main 최종 병합:** PR #3, 커밋 `e20d18a`.
- **현재 검증:** 최신 작업 폴더의 테스트 결과는 [제출 인덱스](../SUBMISSION.md#6-결과물-및-테스트-검증)에 기록합니다. 과거 충돌 해결 시점의 검증과 구분합니다.
- **보완 자료:** 당시 충돌 마커·화면, 원본 해결 명령, 해결 직후 검증 결과.

### 배운 점

공통 `__init__.py`를 통합할 때는 양쪽 공개 함수뿐 아니라 실제 모듈 경로도 확인해야 합니다. PR 작성자, 해결 커밋 작성자, 최종 병합자를 각각 기록하면 기여를 정확하게 구분할 수 있습니다.

---

## 충돌 기록 #2: `utils/string-policy.md`의 공백 제거 정책 동일 줄 충돌 (내용 충돌)

이 기록은 원격 저장소의 실제 Issue·PR·커밋을 기준으로 작성했습니다. 기존에 참조한 `conflict-resolution-scenario.md`는 현재 작업 폴더에 없으므로 원격 증빙 링크를 직접 사용합니다. 이번 실습은 동일 줄 내용 충돌이며, 파일 이동/삭제 대 수정 유형의 비자명 충돌로 분류하지 않습니다.

### 👥 참여자
- **후행 정책 작성 및 PR 생성:** 채민성 (`CMS-SUDO7`), `feature/chae-string-policy-edit`
- **선행 정책 작성:** 고준석 (`kjs83036`), `feature/ko-string-policy-tabs`
- **해결 커밋 작성 및 리뷰:** 고준석. 해결 커밋의 author는 `jun_seok_ko`, committer는 `GitHub`이며, PR #28에 `kjs83036`의 승인 리뷰가 남아 있습니다. 시나리오의 예정 담당자와 실제 기록을 구분했습니다.

### 📌 상황 (What happened)
1. 고준석은 [Issue #21](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/21)·[PR #23](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/23)에서 정책 문서를 추가했습니다. 기준 커밋은 `d8d9a9e`, 병합 커밋은 `42dee7e`입니다.
2. [Issue #22](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/22)·[PR #24](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/24)에서 `docs/conflict-demo/string-policy.md`를 `utils/string-policy.md`로 이동하고 정책을 `스페이스만 제거`로 정했습니다. 이동 커밋은 `1251d9b`, 병합 커밋은 `815eea9`입니다.
3. 두 정책 브랜치는 이동 완료 커밋 `1251d9b`를 공통 출발점으로 삼아 **새 경로의 같은 정책 줄**을 서로 다르게 수정했습니다.
4. 고준석의 [Issue #25](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/25)·[PR #26](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/26)이 먼저 병합되어 `main`의 정책은 `스페이스·탭 제거`가 되었습니다.
5. 채민성의 [Issue #27](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/27)·[PR #28](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/28)은 같은 줄을 `스페이스·탭·줄바꿈 제거`로 변경했습니다. PR 본문과 Issue #27에는 `git merge-tree --write-tree origin/main HEAD`로 `CONFLICT (content)`를 확인했다는 기록이 있습니다. 이 명령은 작업 브랜치에 실제 merge/rebase를 수행하지 않는 사전 확인입니다.

| 구분 | 커밋 | 정책 줄 |
| --- | --- | --- |
| 공통 출발점 | `1251d9b` | 공백 제거 정책: 스페이스만 제거 |
| 고준석 선행 변경 | `9547205` | 공백 제거 정책: 스페이스·탭 제거 |
| 채민성 후행 변경 | `e8e9b24` | 공백 제거 정책: 스페이스·탭·줄바꿈 제거 |

실제 병합 순서는 **PR #23 → #24 → #26 → #28**입니다. 2026-10-01 한국 시간 기준 PR #26은 18:27:55, PR #28은 18:37:46에 병합되었습니다. Issue #27은 기존 push 커밋을 기준으로 같은 날 사후 등록했다고 명시되어 있습니다.

### 🔍 충돌 내용 (Conflict markers)

양쪽 변경에서 충돌한 정책 줄을 설명하면 다음과 같습니다. **아래 마커는 커밋의 정책 문구를 바탕으로 정리한 설명용 예시이며, 실제 GitHub 충돌 편집기 캡처를 전사한 것은 아닙니다.** PR 본문은 채민성 변경의 제목과 정책 줄 끝에 Markdown 줄바꿈용 스페이스 두 칸이 있음을 별도로 기록하고 있습니다.

```text
<<<<<<< feature/chae-string-policy-edit
공백 제거 정책: 스페이스·탭·줄바꿈 제거
=======
공백 제거 정책: 스페이스·탭 제거
>>>>>>> main
```

두 브랜치가 이미 이동된 `utils/string-policy.md`를 수정했으므로, 충돌 원인은 파일 이동이 아니라 동일 줄의 정책 선택입니다.

### 🛠️ 해결 과정 (How)
1. **해결 전략 — 후행 정책 채택:** 최종 파일에는 제거 대상을 `스페이스·탭·줄바꿈`으로 확장한 채민성의 문구를 남겼습니다. 선행 정책의 스페이스·탭 제거 범위를 포함하면서 줄바꿈도 명시하는 선택입니다. 별도의 정책 합의 대화나 상세 선택 이유는 공개 PR 리뷰에서 확인되지 않습니다.
2. **해결 커밋 생성:** `main`을 `feature/chae-string-policy-edit`로 병합한 [해결 커밋 `3df9461`](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/commit/3df9461e945d9997df9888159c6444cf985c0244)이 2026-10-01 18:37:00에 생성되었습니다.
   - 메시지: `Merge branch 'main' into feature/chae-string-policy-edit`
   - 첫 번째 부모(채민성 정책 변경): `e8e9b246f840a9d6793c2ba3726c0dedb423c837`
   - 두 번째 부모(PR #26 병합 후 main): `14c0463299b4072cfbf40d83b51b296aa3a5d929`
   - GitHub가 커미터로 기록된 점은 웹에서 생성한 병합 커밋임을 뒷받침합니다. 다만 `Resolve conflicts` → `Mark as resolved` → `Commit merge` 버튼의 실제 조작 순서와 당시 화면은 보관된 증거에서 확인하지 못했습니다.
3. **리뷰 및 최종 병합:** 고준석은 [승인 리뷰](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/28#pullrequestreview-5377554795)에 `충돌 해결`이라고 남겼습니다. 이후 PR #28이 `main`에 병합되었습니다. 해결 브랜치에 `main`을 병합하는 단계와 PR을 `main`에 최종 병합하는 단계는 별도입니다.

**최종 정책 내용 (`utils/string-policy.md`, 줄 끝 스페이스 생략):**

```text
# 문자열 공백 정책

공백 제거 정책: 스페이스·탭·줄바꿈 제거
```

### 🎯 결과 (Outcome)
- **충돌 해결 커밋:** [`3df9461`](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/commit/3df9461e945d9997df9888159c6444cf985c0244)
- **최종 병합 PR:** [PR #28](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/28), 병합 커밋 [`f8f9fd0`](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/commit/f8f9fd0687c2d6405408ba7c8d01f5acb5ed7f33)
- **원격 결과 확인:** 조회 시점의 `main`에서 `utils/string-policy.md`에 최종 정책이 있고 충돌 마커는 없습니다. 원격 파일 트리에 구 경로 `docs/conflict-demo/string-policy.md`는 없습니다.
- **기존 테스트 결과:** PR #28 본문에는 `python -m pytest -q -p no:cacheprovider` 실행 결과 **22 passed in 0.06s**가 보고되어 있습니다. 이는 PR 작성 시점의 보고이며, 이번 점검에서 현재 작업 폴더의 테스트를 다시 실행한 **22 passed in 3.77s**와 구분합니다. 이번 실행 환경과 명령은 [제출 인덱스](../SUBMISSION.md#6-결과물-및-테스트-검증)에 기록합니다.
- **검증 범위:** 정책 설명 문서만 수정했으며, PR 본문에 따르면 `strip_all_whitespace` 구현은 여전히 스페이스만 제거합니다. 기존 테스트 통과를 탭·줄바꿈 제거 기능의 구현 완료 증거로 해석하지 않습니다.
- **증빙의 한계:** 공개 원격 트리와 현재 작업 폴더에서 충돌 안내·편집기·해결 후 화면 캡처를 확인하지 못했습니다. 충돌 발생 근거는 PR 본문·Issue #27의 사전 확인 기록이고, 해결 및 최종 반영 근거는 해결 커밋·부모 해시·승인 리뷰·병합 PR·최종 파일입니다. 실제 캡처가 있다면 별도로 첨부해야 합니다.

### 💡 배운 점 (Learnings)
- 동일한 이동 완료 커밋에서 분기하고 양쪽이 새 경로의 같은 줄을 다르게 수정하면, 파일 이동 이력과 구분되는 내용 충돌을 재현할 수 있습니다.
- 정책 충돌은 양쪽 문구를 그대로 이어 붙이기보다 최종 적용 범위를 하나의 문구로 정리해야 합니다. 이번 최종 파일은 스페이스·탭·줄바꿈을 모두 명시합니다.
- 해결 커밋의 두 부모를 확인하면 어떤 작업 브랜치와 `main` 사이의 충돌을 정리했는지 추적할 수 있습니다. 화면 캡처는 해결 전에 보관해야 당시 충돌 안내와 편집 과정을 직접 증명할 수 있습니다.
- 정책 문서의 변경과 함수 구현의 변경은 별도로 검증해야 하며, 기존 테스트 통과만으로 새 정책이 구현되었다고 판단할 수 없습니다.


---

## 보충 기록: PR #19의 경로 이동 대 수정

[PR #19](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/19) 본문은 Rename vs Modify 충돌을 해결했다고 기록하고, [승인 리뷰](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/19#pullrequestreview-5208207799)는 신규 함수와 비자명 충돌 해결을 확인했다고 서술합니다. 현재 확인 가능한 Git 객체는 파일 이동과 기능 보존을 보여주며, 당시 충돌 마커·터미널 출력은 확보되지 않았습니다.

| 단계 | 확인된 변경 |
| --- | --- |
| 공통 기준 `4de1655` | 문자열 구현이 `src/string_ops.py`에 있음 |
| 기능 변경 `08da39a` | 구 경로에 `slugify`, `truncate_words` 추가 |
| main 변경 `556a6c5` | PR #14를 통해 `src/utils/`로 모듈 이동 |
| 작업 브랜치 병합 `8c0c9cd` | 부모 `08da39a`, `556a6c5`; 신규 함수를 새 경로에 보존 |
| 최종 병합 `d3d4bc9` | PR #19가 main에 반영됨 |

PR 작성자는 채민성이며, `8c0c9cd`의 Git author는 고준석입니다. 해당 커밋과 첫 부모의 diff에서 `src/string_ops.py` → `src/utils/string_ops.py`는 내용이 같은 100% rename으로 표시됩니다. main 쪽 부모와 비교하면 새 경로에 두 신규 함수가 추가되어 있습니다. 이 결과는 기능 이관을 확인하는 자료이며 수동 충돌 발생 자체를 입증하는 원본 자료는 아닙니다.

```bash
# 두 작업의 공통 기준과 병합 부모 확인
git merge-base 08da39a 556a6c5
git show --no-patch --format=fuller 8c0c9cd
# 구 경로의 기능이 새 경로에 보존되었는지 확인
git diff --find-renames 8c0c9cd^1 8c0c9cd -- src/string_ops.py src/utils/string_ops.py
git diff 8c0c9cd^2 8c0c9cd -- src/utils/string_ops.py
```

위 명령은 확인 방법이며 원본 실행 로그가 아닙니다. 비자명 충돌의 직접 증빙을 완성하려면 당시 충돌 메시지·마커 또는 화면, 실제 해결 명령과 검증 결과를 추가해야 합니다. 정책 문서의 동일 줄 내용 충돌과 구분하여 제출합니다.

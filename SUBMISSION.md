# 📋 Submission Index (제출물 인덱스)

**과제명:** B2-2 친구 3~5명과 함께 프로그램 만드는 법 연습하기  
**분야:** AI/SW 기초 | Python과 Git 심화  
**최신화 기준:** 2026-10-01 (한국 시간)

원격 협업 기록은 [PR #30 병합 커밋 `070d3e5`](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/commit/070d3e52e703f29aa8d1eeeb991a2ea57b7e17a6)까지 GitHub API로 확인했습니다. 코드·테스트는 현재 작업 폴더에서 확인했으며, 원본 실습 로그와 별도 재현을 구분합니다. 모든 항목의 충족을 일괄 단정하지 않고 확인된 결과와 보완 사항을 아래에 기록합니다.

## 1. 팀 정보

- **팀명:** Codyssey Teamwork B2-2 (ko-park-chae)
- **저장소:** [AI-SW-Basic-B2-2](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2)

| 팀원 | GitHub 계정 | Git Author 표기 예 | 주요 기여 |
| --- | --- | --- | --- |
| 고준석 | [kjs83036](https://github.com/kjs83036) | `jun_seok_ko`, `고준석` | 수학 모듈, 패키지 재배치, 정책 문서, 리뷰 및 충돌 해결 |
| 채민성 | [CMS-SUDO7](https://github.com/CMS-SUDO7) | `CMS_SUDO7` | 문자열 모듈, 고급 문자열 함수, 정책 변경 PR |
| 박영세 | [MetaStudy999](https://github.com/MetaStudy999) | `metastudy999` | 날짜 모듈, 테스트 스위트, revert 기록, 리뷰 |

GitHub 로그인과 로컬 Git Author 표기는 다를 수 있으므로 PR 작성자는 GitHub 계정으로 집계했습니다.

## 2. 팀원별 PR 및 리뷰

확인된 병합 PR은 **총 15개**입니다. 승인 리뷰는 GitHub의 `APPROVED` 리뷰 제출을 기준으로 세며, PR 본문 아래 일반 코멘트는 별도로 표시합니다.

| 팀원 | 작성·병합 PR | 승인 리뷰를 남긴 PR | 추가 리뷰 코멘트 |
| --- | --- | --- | --- |
| 고준석 | 9개: #2, #5, #9, #12, #14, #23, #24, #26, #30 | 6개: #3, #11, #16, #19, #20, #28 | #3의 테스트 추가 요청 등 |
| 채민성 | 3개: #3, #19, #28 | 7개: #9, #11, #12, #23, #24, #26, #30 | #2의 기능·테스트 보완 요청 |
| 박영세 | 3개: #11, #16, #20 | 4개: #2, #3, #9, #14 | #3의 경로·공백 처리 보완 제안 |

### 고준석 (`kjs83036`)

| 병합 PR | 제목 | 작업 브랜치 |
| --- | --- | --- |
| [#2](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/2) | feat: add math utility functions and exports | `feature/ko-math-utils` |
| [#5](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/5) | add contributing docs | `feature/ko-math-utils` |
| [#9](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/9) | fix:from math_ops, test_math_ops fix path | `feature/ko-math-utils` |
| [#12](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/12) | fix: math_ops에 calculate_average 함수 구현 및 __init__ export 누락 해결 | `feature/ko-math-utils` |
| [#14](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/14) | refactor: restructure package modules into src/utils/ directory layout | `refactor/kim-package-structure` |
| [#23](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/23) | docs: add string policy conflict exercise | `feature/ko-string-policy-base` |
| [#24](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/24) | docs: move string policy and define whitespace rule | `feature/ko-string-policy-move` |
| [#26](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/26) | docs: 문자열 정책에서 탭도 제거 | `feature/ko-string-policy-tabs` |
| [#30](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/30) | docs: 협업 가이드와 제출 문서 정비 | `docs/ko-document-update` |

승인 리뷰: [#3](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/3#pullrequestreview-4980559580), [#11](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/11#pullrequestreview-4981416503), [#16](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/16#pullrequestreview-5207827067), [#19](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/19#pullrequestreview-5208207799), [#20](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/20#pullrequestreview-5208571516), [#28](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/28#pullrequestreview-5377554795).

**피드백 반영:** PR #2의 [채민성 요청](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/2#issuecomment-5327442102)에 따라 사칙연산·테스트를 추가한 `dcebd66`, export를 보완한 `62df08e`, 범위 밖 함수를 제거한 `80e72e2`가 있습니다. [작성자 답글](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/2#issuecomment-5327946568)과 [리뷰어 확인](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/2#issuecomment-5327583975)도 남아 있습니다.

### 채민성 (`CMS-SUDO7`)

| 병합 PR | 제목 | 작업 브랜치 |
| --- | --- | --- |
| [#3](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/3) | string_ops.py __init__.py test_string_ops.py 구현 | `feature/chae-string-utils` |
| [#19](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/19) | feat: add slugify and truncate_words utilities | `feature/chae-advanced-strings` |
| [#28](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/28) | docs: 문자열 공백 정책을 스페이스·탭·줄바꿈 제거로 변경 | `feature/chae-string-policy-edit` |

승인 리뷰: [#9](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/9#pullrequestreview-4980726109), [#11](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/11#pullrequestreview-4981422724), [#12](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/12#pullrequestreview-5206660386), [#23](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/23#pullrequestreview-5376917929), [#24](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/24#pullrequestreview-5376924772), [#26](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/26#pullrequestreview-5377443603), [#30](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/30#pullrequestreview-5378076355). PR #2는 일반 코멘트로 리뷰에 참여했습니다.

**피드백 반영:** PR #3의 [테스트 추가 요청](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/3#issuecomment-5328721461) 뒤 `e2e4471`에서 테스트가 추가됐고 [리뷰어 확인](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/3#issuecomment-5352869108)이 있습니다. `7f70335`의 경로 수정도 확인됩니다. 다만 [박영세의 탭·줄바꿈 제거 제안](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/3#issuecomment-5353121730)은 현재 구현에 반영되지 않았습니다. PR #28의 작성자는 채민성이지만 충돌 해결 커밋 `3df9461`의 author는 고준석(`jun_seok_ko`)입니다.

### 박영세 (`MetaStudy999`)

| 병합 PR | 제목 | 작업 브랜치 |
| --- | --- | --- |
| [#11](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/11) | add command, add date_ops, add test, fix __init__ | `feature/park-date-utils` |
| [#16](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/16) | docs: add relative time calculation work note | `feature/park-date-utils` |
| [#20](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/20) | test: add comprehensive test suite across all modules | `feature/park-test-suite` |

승인 리뷰: [#2](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/2#pullrequestreview-4960818608), [#3](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/3#pullrequestreview-4980566630), [#9](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/9#pullrequestreview-4980779358), [#14](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/pull/14#pullrequestreview-5207960482).

**피드백 반영 확인 범위:** `90f1535`에서 export 수정과 날짜 테스트 경로 정리가 확인됩니다. 다만 PR #11의 현재 코멘트·리뷰만으로는 박영세가 받은 구체적인 요청과 해당 수정의 연결, 작성자 답글을 확인하기 어렵습니다. 전원 피드백 반영 요건을 확정하려면 추가 증빙이 필요합니다. PR #16의 WIP 주석은 상대 시간 함수 구현이나 stash 수행의 증거로 집계하지 않습니다.

### 팀원별 작성 Issue

2026-10-01 GitHub API에서 확인한 **실제 Issue 작성자** 기준입니다. PR 작성자와 연결 Issue 작성자는 다를 수 있습니다.

| 팀원 | 작성 Issue |
| --- | --- |
| 고준석 | [#1](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/1), [#7](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/7), [#13](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/13), [#21](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/21), [#22](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/22), [#25](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/25), [#29](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/29) |
| 채민성 | [#4](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/4), [#18](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/18), [#27](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/27) |
| 박영세 | [#6](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/6), [#8](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/8), [#10](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/10), [#15](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/15) (열림) |

PR #5는 연결 없음, #16은 `Refs #15`, #20은 종료 키워드 자리표시자로 남아 있습니다. 

## 3. 핵심 문서 및 구현

- [전체 Git 그래프](docs/evidence/git-log.txt): 실제 `git log --oneline --graph --all --decorate` 출력
- [README.md](README.md): 실제 API, 사용 예시, 환경 설정 및 테스트 안내
- [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md): 브랜치·커밋·PR·리뷰 협업 규칙
- [docs/conflict-resolution.md](docs/conflict-resolution.md): Export 통합·정책 내용 충돌 및 PR #19 경로 이동 보충 기록
- [docs/troubleshooting-log.md](docs/troubleshooting-log.md): Git 4종 원본 증빙 확인 범위와 독립 클론 재현
- [utils/string-policy.md](utils/string-policy.md): 현재 작업 브랜치의 정책 문서
- [Python 가상환경·pytest 명령](docs/command/python_venv_pytest.md), [Issue 생성 명령](docs/command/gh_issue_create.md), [PR 생성 명령](docs/command/gh_pr_create.md)

### 충돌 증빙 구분

| 기록 | 유형 및 파일 | 증빙 | 확인 범위 |
| --- | --- | --- | --- |
| 문서 기록 #1 | Export 통합, 과거 `src/__init__.py` | PR #3, 해결 커밋 `2847fe1`, 최종 병합 `e20d18a` | 두 모듈 export 통합 확인; 당시 충돌 마커·실행 로그 미확보, import 경로 불일치도 구분 |
| 문서 기록 #2 | 동일 줄 내용 충돌, `utils/string-policy.md` | PR #26·#28, 해결 커밋 `3df9461`, 최종 병합 `f8f9fd0` | 최종 정책 및 부모 커밋 확인; 당시 화면 캡처 미확보 |
| 문서 보충 기록 | 경로 이동 대 수정, `src/string_ops.py` → `src/utils/string_ops.py` | PR #19 본문·승인 리뷰, 병합 커밋 `8c0c9cd` | 공통 기준·두 부모·기능 이관 결과 기록; 당시 충돌 원본 자료 미확보 |

PR #23·#24는 정책 문서 추가·이동, PR #26·#28은 **이동 완료 후 같은 새 경로의 정책 줄을 수정**한 작업입니다. 정책 충돌을 Rename vs Modify로 분류하지 않습니다. 원문은 같은 hunk를 서로 다르게 수정한 충돌도 비자명 충돌로 인정하므로 PR #26·#28의 정책 충돌이 해당 유형입니다. [현재 재현 로그](docs/evidence/conflict-2-reproduction.txt)로 충돌을 확인했으며, 당시 수행 로그와 이번 재현을 구분합니다.

`conflict-resolution-scenario.md`는 작업 폴더와 확인한 원격 트리에 없습니다. 충돌 문서의 깨진 링크를 제거하고 실제 PR·커밋을 직접 연결했습니다. 당시 충돌 화면·마커 원본·실제 해결 명령은 제출 전에 보완할 항목입니다.

### 트러블슈팅 증빙 구분

| 실습 | 원본 수행 증빙 | 별도 재현 |
| --- | --- | --- |
| `commit --amend` | 원본 터미널·reflog 미확보; `cbdf63c`만으로 수행 여부 확인 불가 | 독립 클론의 amend 동작 기록 |
| `reset --soft` | 시작 해시 `9f8e7d6` 확인 불가; `08da39a`는 기능 커밋 | 실제 브랜치 HEAD에서 혼합 커밋 분리 흐름 재현 |
| `revert` | `b9c1222`를 되돌린 원격 커밋 `ebce9a2` 확인 | 독립 클론에서 3줄 삭제를 재현 |
| `stash` / `stash pop` | 원본 stash 객체·세션 미확보; `6404b67`은 문서 커밋 | 독립 클론의 임시 WIP 주석 보관·복원 기록 |

별도 재현은 명령 동작을 확인한 자료이며 당시 수행자와 원래 작업 내용을 입증하는 원본 로그를 대체하지 않습니다.

## 4. 최신 Git 이력 증빙

확인한 원격 `main`의 최신 병합 순서는 **PR #20 → #23 → #24 → #26 → #28 → #30**입니다.

| PR | 변경 커밋 / 해결 커밋 | `main` 병합 커밋 | 병합 시각 (한국 시간) |
| --- | --- | --- | --- |
| #20 | `55bef12` | `ef6dc51` | 2026-09-15 19:17:16 |
| #23 | `d8d9a9e` | `42dee7e` | 2026-10-01 17:39:56 |
| #24 | `1251d9b` | `815eea9` | 2026-10-01 17:40:45 |
| #26 | `9547205` | `14c0463` | 2026-10-01 18:27:55 |
| #28 | `e8e9b24` / `3df9461` | `f8f9fd0` | 2026-10-01 18:37:46 |
| #30 | `6a88feb` / `0eb5cf8` / `984909b` / `0b45ff1` | `070d3e5` | 2026-10-01 19:31:12 |

정책 충돌 해결 커밋 [`3df9461`](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/commit/3df9461e945d9997df9888159c6444cf985c0244)의 부모는 후행 정책 커밋 `e8e9b24`와 PR #26 병합 후 `main`인 `14c0463`입니다. 이후 PR #28의 병합 커밋 `f8f9fd0`에 반영됐습니다.

원격 최종 정책과 현재 작업 폴더의 정책은 **스페이스·탭·줄바꿈 제거**입니다. 현재 로컬 브랜치는 `docs/ko-document-update`, HEAD는 `0b45ff1`입니다. 로컬 `main`과 저장된 `origin/main`은 `f8f9fd0`이며, API로 재확인한 원격 `main`은 PR #30 병합 후 `070d3e5`입니다. 원격 조회와 로컬 참조를 구분합니다.

**제출 증빙:** [전체 실제 로컬 그래프](docs/evidence/git-log.txt). 2026-10-01 `git log --oneline --graph --all --decorate`로 실행한 결과이며, 명령 안내만 남긴 상태를 보완했습니다. 원격 PR #30은 현재 로컬 참조에 없어 아래 그래프 파일에 포함되지 않습니다. 이번 미커밋 변경 역시 그래프에 포함되지 않습니다.

최신 그래프를 다시 확인할 때는 작업 상태를 확인한 뒤 다음 명령을 사용합니다.

```bash
git status --short --branch
git fetch origin
git log --oneline --graph --all --decorate
```

위 명령은 향후 재확인 방법입니다. 이번 실제 실행 결과는 위 전체 그래프 링크에 저장했습니다. 이번 검토에서는 `git fetch`를 수행하지 않았습니다.

## 5. 브랜치 보호 규칙 증빙

2026-10-01 GitHub Ruleset API 조회 결과입니다.

| 규칙 | 상태 / 대상 | 설정 내용 |
| --- | --- | --- |
| [base_rule (21023839)](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/rules/21023839) | `active`, `~DEFAULT_BRANCH` (`main`) | 삭제·강제 푸시 제한, PR 필수, 승인 리뷰 1명 |
| [protection_rule (20982995)](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/rules/20982995) | `active`, 대상 include 목록 비어 있음 | 동일한 삭제·강제 푸시·PR 규칙 정의; 이 응답만으로 `main`에 중복 적용된다고 단정하지 않음 |

`base_rule`에는 조직 관리자(`OrganizationAdmin`)의 상시 우회가 설정되어 있습니다. 따라서 모든 사용자에게 직접 push가 절대 차단된다고 표현하지 않습니다. `required_review_thread_resolution`은 `false`이고 필수 상태 검사 규칙은 없습니다. 미해결 코멘트 해소와 테스트 통과는 [협업 가이드](docs/CONTRIBUTING.md)의 팀 운영 기준입니다. 확인한 원격 트리에는 `.github/workflows/`가 없습니다.

PR #5는 승인 리뷰 제출 기록 없이 병합되어, 모든 과거 PR이 최소 승인 요건을 충족했다고 단정할 수 없습니다.

## 6. 결과물 및 테스트 검증

- 공개 API: 수학 6개, 문자열 5개, 날짜 2개로 총 **13개**. `src/utils/__init__.py`에서 export합니다.
- 이번 실행 환경: Python **3.12.14**, pytest **9.1.1**의 임시 가상환경.
- 검증 대상: 현재 작업 폴더(HEAD `0b45ff1`)의 코드와 테스트. 원격 `main` 체크아웃에 대한 재실행 결과는 아닙니다.

```bash
PYTHONDONTWRITEBYTECODE=1 /private/tmp/b2-2-docs-check-20261001/bin/python -m pytest tests/ -q -p no:cacheprovider
```

```text
22 passed in 0.04s
```

| 테스트 파일 | 개수 | 검증 내용 |
| --- | --- | --- |
| `tests/test_math_ops.py` | 7 | 사칙연산, 0 나누기 기본값, 거듭제곱, 음수, 빈 평균, 제너레이터 |
| `tests/test_string_ops.py` | 9 | 빈 문자열, 한글 반전, slug, 단어 축약·접미사, 대문자화, 스페이스 제거 |
| `tests/test_date_ops.py` | 6 | 날짜 포맷, 현재 날짜 대체, 윤일, 음수·0 일수, 연도 경계 |

테스트 통과는 기존 기능의 회귀 검증입니다. `strip_all_whitespace`의 탭·줄바꿈 제거 테스트와 해당 구현은 없습니다. `parse_date_string`, `get_relative_time_string`도 구현되어 있지 않으며 [Issue #15](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/15)는 확인 시점에 열려 있습니다.

## 7. 과제 요구사항 자가 검증 및 보완 항목

- [x] **팀 구성·기본 구조:** 3인 참여, `docs/`, `src/utils/`, `tests/` 구성.
- [x] **브랜치 보호 설정:** `main` 대상 활성 ruleset에 PR 및 승인 1명 요건 확인. 관리자 우회 예외는 위에 명시.
- [x] **PR·리뷰 최소 수량:** 팀원별 병합 PR 9/3/3개, 승인 리뷰 6/7/4개로 각 2개 이상.
- [x] **Git 히스토리 증빙:** 전체 실제 로컬 그래프를 `docs/evidence/git-log.txt`에 저장하고 README·인덱스에서 연결.
- [x] **팀원별 Issue 인덱스:** 실제 작성자별 Issue 링크 목록 추가.
- [x] **구현·기존 테스트:** 모듈 3종, 공개 API 13개, 현재 작업 폴더의 테스트 22개 통과.
- [ ] **전원 피드백 반영 증빙:** 고준석·채민성의 요청과 수정은 확인. 박영세의 요청–수정–답글 연결 자료 보완 필요.
- [x] **브랜치 전략 문서화:** main·작업 브랜치, 네이밍 규칙 및 GitHub Flow 선택 이유 기록. 과거 PR #14의 `kim` 별칭은 당시 가이드 예시에 있었으므로 현재 `ko` 규칙을 소급 적용하여 위반으로 판정하지 않음.
- [ ] **Issue–PR 종료 키워드:** PR #5는 연결 이슈 없음, PR #16은 `Refs #15`이며 Issue #15는 열려 있음. PR #20은 `Closes #이슈번호` 자리표시자가 남아 있음.
- [ ] **커밋 메시지 규칙:** 과거 `chore:fix templete path`(`85de3fc`) 등 형식 예외와 변경 목적이 불명확한 메시지 보완 필요.
- [ ] **리뷰 품질·상호작용:** PR #2·#3에 구체적 제안이 있으나 일반 코멘트 형태. 확인한 PR #2·#3·#11·#12에는 인라인 리뷰 코멘트가 없고, PR #9의 채민성 승인 본문은 비어 있음. 원문은 특정 파일 근거의 일반 댓글도 허용하므로 인라인 부재 자체는 미충족 사유가 아님. PR #5 리뷰·댓글 없음, #30 단순 확인만 있어 실질 리뷰·상호작용은 전부 충족하지 않음.
- [ ] **충돌 2회 및 비자명 충돌 문서화:** Export 통합과 정책 내용 충돌, PR #19의 경로 이동·기능 보존 결과를 문서에 기록. 부모 커밋으로 Export·같은 hunk 정책 충돌을 재현하여 현재 로그 첨부. 정책 충돌은 원문의 비자명 기준에 해당. 당시 실제 해결 명령·검증 결과 보완 필요; 화면 캡처 자체를 일괄 필수로 요구하지 않음.
- [ ] **Git 트러블슈팅 4종 원본 증빙:** revert 커밋 확인, amend/reset/stash는 원본 로그 미확보. 독립 클론 재현과 원본 실습을 구분하여 제출.
- [ ] **협업 가이드 분담:** 내용은 갖추었으나 파일 변경 커밋은 고준석 계정만 확인. 팀원 분담 작성 증빙 필요.
- [ ] **PR 본문:** PR #3의 What/Why/How 누락 보완 필요.
- [ ] **정책과 구현 일치:** 원격 최종 정책의 탭·줄바꿈 제거를 함수 및 테스트에 반영하는 후속 작업 필요.

이번 최신화는 README·제출 인덱스와 docs의 협업·명령어·충돌·트러블슈팅 문서를 정리하고 현재 테스트를 다시 확인한 작업입니다. 위 보완 항목은 아직 수행·구현·증빙 확보가 필요한 상태로 남겨 둡니다.

# 🛠️ Team Python Utility Toolkit (AI-SW-Basic-B2-2)

고준석·채민성·박영세가 GitHub Flow, Issue–PR 연동, 코드 리뷰, 충돌 해결 및 Git 트러블슈팅을 연습하며 만든 Python 유틸리티 라이브러리입니다. 수학·문자열·날짜 모듈의 공개 함수 13개와 단위 테스트 22개를 포함합니다.

**최신화 기준: 2026-10-01 (한국 시간).** 원격 협업 이력은 [PR #30 병합 커밋 `070d3e5`](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/commit/070d3e52e703f29aa8d1eeeb991a2ea57b7e17a6)까지 확인했습니다. 구현·테스트 설명은 현재 작업 폴더의 코드를 기준으로 작성했습니다. 제출 증빙과 보완 항목은 [SUBMISSION.md](SUBMISSION.md)에 정리합니다.

## 🎯 과제 소개 및 학습 목표

`친구 3~5명과 함께 프로그램 만드는 법 연습하기.md`의 요구사항을 기준으로 진행하는 **AI/SW 기초 · Python과 Git 심화** 과제입니다. 권장 학습시간은 **20시간**이며, 우리 팀은 고준석·채민성·박영세 **3인**으로 GitHub Organization 저장소에서 협업합니다.

선택한 결과물은 **(A) 팀원별 유틸 함수 모음**입니다. 각 팀원은 담당 모듈의 함수와 사용 예시에 기여합니다. `team/` 폴더는 팀 소개 결과물 (B)을 선택할 때 사용하는 선택 항목입니다. 이 과제의 핵심은 복잡한 기능보다 **Issue → 작업 브랜치 → PR → 리뷰 → 수정 → 병합** 과정과 재현 가능한 문제 해결 기록을 남기는 데 있습니다.

- 브랜치가 커밋을 가리키는 포인터라는 점과 작업별 브랜치를 나누는 이유를 설명합니다.
- GitHub Flow와 PR 기반 코드 리뷰의 목적을 이해하고 팀 규칙에 따라 협업합니다.
- 충돌 원인과 `<<<<<<<`, `=======`, `>>>>>>>` 마커의 의미를 이해하고 해결 과정을 기록합니다.
- `reset`, `revert`, `stash`의 차이를 설명하고 상황에 맞는 명령을 선택합니다.

## 📌 GitHub Flow 채택 이유

1. `main`과 작업 브랜치 중심으로 변경 흐름을 단순하게 유지합니다.
2. Issue와 PR로 작업 목적을 연결하고, 팀원 리뷰와 테스트 결과를 확인한 뒤 병합합니다.
3. 작은 단위로 변경을 공유하여 충돌과 피드백을 빠르게 처리합니다.

협업 규칙은 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)를 따릅니다. `main`에는 PR 및 승인 1명 요건이 설정되어 있으며, 테스트 통과는 팀 협업 규칙입니다. 현재 GitHub Actions 워크플로와 필수 상태 검사 설정은 없습니다. 상세 규칙과 예외는 [제출 인덱스](SUBMISSION.md#5-브랜치-보호-규칙-증빙)를 참고합니다.

### 팀 작업 순서

1. 작업 목적·범위·완료 조건을 Issue에 작성하고 담당자를 정합니다.
2. 최신 `main`에서 `<type>/<member_name>-<feature-name>` 형식의 브랜치를 만듭니다. 예: `feature/ko-math-utils`.
3. 기능과 테스트를 작성하고 `feat: 평균 계산 함수 추가`처럼 대상과 목적이 드러나는 메시지로 커밋합니다. `update`, `fix`, `wip` 같은 단어만 사용하지 않습니다.
4. PR에 **What / Why / How**와 `Closes #<실제 이슈번호>` 또는 `Fixes #<실제 이슈번호>`를 작성합니다. [PR 템플릿](.github/pull_request_template.md)을 사용하고 자리표시자는 실제 번호로 바꿉니다.
5. 다른 팀원이 특정 파일·라인을 근거로 질문, 대안 또는 개선 의견을 남깁니다. 작성자는 답글과 수정 커밋으로 반영 결과를 기록합니다.
6. 최소 1명 승인, 테스트 통과, 미해결 코멘트 해소를 확인한 뒤 PR로 `main`에 병합하고 제출 인덱스를 갱신합니다.

공유 브랜치의 히스토리를 무리하게 재작성하지 않으며, 팀 합의 없이 강제 푸시나 리베이스를 수행하지 않습니다.

### 팀원별 최소 기여 기준

아래 기준은 **모든 팀원이 각각** 충족해야 합니다. 수량은 [제출 인덱스의 2026-10-01 API 재조회 집계](SUBMISSION.md#2-팀원별-pr-및-리뷰)를 기준으로 하며, 리뷰 품질과 피드백 반영 증빙은 별도로 확인합니다.

| 항목 | 과제 최소 기준 | 현재 문서에 기록된 상태 |
| --- | --- | --- |
| PR 작성 및 병합 | 각 2개 이상 | 고준석 9개 / 채민성 3개 / 박영세 3개 |
| 타인 PR 리뷰 | 각 2개 이상, 본인 PR 제외 | 승인 리뷰 고준석 6개 / 채민성 7개 / 박영세 4개 |
| 본인 PR의 리뷰 반영 | 각 1회 이상, 커밋·수정·답글로 증빙 | 고준석·채민성·박영세 연결 기록 있음 |
| 트러블슈팅 기록 참여 | 각 1개 시나리오 이상, 이름·역할 명시 | 문서에 참여자·역할 명시; 원본 수행 증빙 보완 필요 |
| 선택한 결과물 기여 | 각 함수 1개 이상과 기여 커밋 1건 이상 | 수학·문자열·날짜 모듈별 함수 및 커밋 기록 있음 |

과제 원문은 **각 PR에 실질 코멘트 1개 이상과 리뷰어–작성자 상호작용 1회 이상**을 요구합니다. 단순 승인 수량만으로 이 기준을 충족했다고 판단하지 않습니다. 팀 협업 가이드는 특정 라인을 지정하는 리뷰를 추가 운영 기준으로 정하고 있습니다.

## 🚀 구현된 기능 및 담당자

| 모듈 | 공개 함수 | 담당자 / GitHub 계정 |
| --- | --- | --- |
| `src.utils.math_ops` | `add`, `subtract`, `multiply`, `divide`, `power`, `calculate_average` | 고준석 / [kjs83036](https://github.com/kjs83036) |
| `src.utils.string_ops` | `capitalize_words`, `reverse_string`, `strip_all_whitespace`, `slugify`, `truncate_words` | 채민성 / [CMS-SUDO7](https://github.com/CMS-SUDO7) |
| `src.utils.date_ops` | `format_iso_date`, `add_days_to_date` | 박영세 / [MetaStudy999](https://github.com/MetaStudy999) |

- `divide(a, 0)`은 예외 대신 `default` 값(기본 `0.0`)을 반환합니다.
- `calculate_average([])`는 `0.0`을 반환하며, 리스트 외에 제너레이터 등 이터러블도 받습니다.
- `format_iso_date()`는 현재 시스템 날짜를 `YYYY-MM-DD`로 반환합니다. `add_days_to_date()`는 음수 일수도 받으며 시간 값을 보존합니다.
- `slugify()`는 소문자 변환, 문장부호 제거, 공백·밑줄·하이픈 정리를 수행합니다. 한글 등 유니코드 단어 문자는 유지합니다.
- `truncate_words()`는 단어 수를 초과할 때 접미사(기본 `...`)를 붙입니다.

### 구현 범위와 후속 작업

`strip_all_whitespace()`는 현재 ASCII 스페이스(`" "`)만 제거하고 탭·줄바꿈은 유지합니다. [utils/string-policy.md](utils/string-policy.md)와 원격 `main`의 [최종 정책 문서](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/blob/f8f9fd0687c2d6405408ba7c8d01f5acb5ed7f33/utils/string-policy.md)는 스페이스·탭·줄바꿈 제거를 명시하므로 구현 및 테스트 보완이 필요합니다.

날짜 파싱(`parse_date_string`)과 상대 시간 계산(`get_relative_time_string`)은 구현되어 있지 않습니다. 상대 시간 작업은 WIP 주석만 있으며 [Issue #15](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/15)는 확인 시점에 열려 있습니다.

## 💻 개발 및 테스트

- 과제의 환경 기준은 Python 3.10 이상이며, 이 저장소의 권장 환경은 Python 3.12입니다. 기존 검증은 Python **3.12.14**, pytest **9.1.1**로 실행했습니다.
- 실행 코드의 외부 의존성은 없으며, 테스트에는 `pytest`가 필요합니다.
- 설치용 패키지 설정 파일은 없으므로 저장소 루트에서 실행합니다.

### 환경 설정 및 실행

```bash
git clone https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2.git
cd AI-SW-Basic-B2-2

# Python 3.12가 설치된 환경에서 가상환경 생성
python3.12 -m venv .venv
source .venv/bin/activate

python -m pip install pytest
python -m pytest tests/ -v
```

Windows PowerShell에서는 `py -3.12 -m venv .venv`로 생성하고 `.\.venv\Scripts\Activate.ps1`로 활성화합니다. Ubuntu의 가상환경 설정은 [명령어 가이드](docs/command/python_venv_pytest.md)를 참고합니다.

2026-10-01 현재 작업 폴더에서 `python -m pytest tests/ -q -p no:cacheprovider`로 **22개 통과**를 확인했습니다(수학 7개, 문자열 9개, 날짜 6개). 탭·줄바꿈 제거를 검증하는 테스트는 아직 없습니다.

### 사용 예시

```python
from datetime import datetime

from src.utils import (
    add_days_to_date,
    calculate_average,
    divide,
    format_iso_date,
    slugify,
    strip_all_whitespace,
    truncate_words,
)

assert calculate_average([2, 4, 6]) == 4.0
assert divide(10, 0, default=-1) == -1
assert slugify("Hello, World!") == "hello-world"
assert truncate_words("one two three", 2) == "one two..."
assert strip_all_whitespace(" a\tb\nc ") == "a\tb\nc"

next_day = add_days_to_date(datetime(2024, 2, 28, 10, 30), 1)
assert format_iso_date(next_day) == "2024-02-29"
```

## 📁 디렉터리 구조

```text
AI-SW-Basic-B2-2/
├── .github/
│   ├── ISSUE_TEMPLATE/feature_request.md
│   └── pull_request_template.md
├── docs/
│   ├── command/                  # 이슈·PR 생성 및 가상환경 명령어
│   ├── CONTRIBUTING.md           # 협업 규칙
│   ├── conflict-resolution.md    # 충돌 해결 기록 2건
│   └── troubleshooting-log.md    # Git 4종 기록 및 별도 재현
├── src/utils/
│   ├── __init__.py               # 공개 함수 13개 export
│   ├── date_ops.py
│   ├── math_ops.py
│   └── string_ops.py
├── tests/
│   ├── test_date_ops.py          # 6개
│   ├── test_math_ops.py          # 7개
│   └── test_string_ops.py        # 9개
├── utils/string-policy.md        # 문자열 공백 정책 문서
├── README.md
└── SUBMISSION.md                 # 제출물 인덱스
```

루트 `utils/`는 정책 문서 디렉터리이며 Python 함수는 `src/utils/`에 있습니다.

## 📑 협업 및 제출 문서

- [협업 가이드](docs/CONTRIBUTING.md)
- [충돌 해결 기록](docs/conflict-resolution.md): Export 통합과 공백 정책 동일 줄 내용 충돌, PR #19의 경로 이동·기능 보존 보충 기록. 원본 충돌 증빙과 Git 객체로 확인한 결과를 구분합니다.
- [Git 트러블슈팅 기록](docs/troubleshooting-log.md): amend/reset/revert/stash의 원본 증빙과 독립 클론 재현을 구분합니다.
- [제출물 인덱스](SUBMISSION.md): 팀원별 PR·리뷰, 최신 이력, 규칙 설정 및 보완 체크리스트.

## ✅ 과제 제출 확인 항목

| 필수 산출물·실습 | 확인 위치 및 보완 사항 |
| --- | --- |
| 팀 GitHub 저장소 URL | [AI-SW-Basic-B2-2](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2) |
| 팀원별 Issue·PR·문서·증빙 인덱스 | [SUBMISSION.md](SUBMISSION.md): 팀원별 작성 Issue·PR 목록 정리 완료; PR #5·#16·#20의 Issue 연결·종료 키워드 보완 필요 |
| 협업 규칙 3종 문서 | [협업 가이드](docs/CONTRIBUTING.md), [충돌 기록](docs/conflict-resolution.md), [트러블슈팅 기록](docs/troubleshooting-log.md) |
| Git 히스토리 증빙 | [전체 실제 로그](docs/evidence/git-log.txt) 및 아래 `git log --oneline --graph --all --decorate` 명령·출력 |
| 팀 전체 충돌 해결 2회 이상 | Export 통합·공백 정책 충돌 기록 있음; 당시 마커·실제 해결 절차·검증 결과 보완 |
| 비자명 충돌 1회 이상 | 원문은 **같은 파일의 같은 hunk를 서로 다르게 수정**하거나 **이동·이름 변경·삭제 대 내용 수정** 중 하나를 인정. 정책 동일 줄 충돌은 첫 유형에 해당하며 원본 증빙 보완 필요 |
| Git 트러블슈팅 4종 | `commit --amend`, `reset --soft HEAD~1`, `revert`, `stash` / `stash pop`: 문서의 원본 기록과 독립 클론 재현을 구분하여 제출 |
| 유틸 함수 및 사용 예시 | 위 담당자 표와 Python 사용 예시; 각 팀원의 기여 커밋은 제출 인덱스에서 확인 |

**충돌 판정 기준:** 파일 이동 대 수정만 비자명 충돌로 인정하는 것은 아닙니다. 과제 원문의 기준에 따라 공백 정책의 동일 줄 충돌도 대상이 됩니다. 다만 설명용 충돌 마커를 당시 실제 수행 로그로 제출하지 않으며, 충돌 기록에는 참여자·상황·충돌 내용·해결 전략과 이유·실제 절차·결과·배운 점을 남깁니다. 트러블슈팅도 참여자·상황·명령·결과·주의점·방법 선택 이유를 기록합니다.

선택 보너스는 개인 feature 브랜치의 `git rebase -i` 전후 비교와 `.github/CODEOWNERS`를 통한 책임 리뷰어 지정입니다. 현재 README에서는 보너스를 완료 항목으로 집계하지 않습니다.

### Git 히스토리 증빙

저장소 루트에서 다음 명령을 실행했습니다.

```bash
git log --oneline --graph --all --decorate
```

[전체 실제 실행 결과 텍스트](docs/evidence/git-log.txt)를 제출 증빙으로 제공합니다. 아래는 동일 출력의 앞 15줄이며, 전체 그래프는 링크에서 확인합니다. 2026-10-01 실행 시 로컬 브랜치는 `docs/ko-document-update`, HEAD는 `0b45ff1`입니다. 로컬 참조 기준이며, 별도로 API 확인한 원격 main은 PR #30 병합 후 `070d3e5`입니다. 줄 끝 공백만 제거했으며 이번 미커밋 문서 변경은 로그에 포함되지 않습니다.

```text
* 0b45ff1 (HEAD -> docs/ko-document-update, origin/docs/ko-document-update) docs: Git 트러블슈팅 증빙 정리
* 984909b docs: 충돌 해결 근거 기록
* 0eb5cf8 docs: 협업 및 Git 명령 가이드 갱신
* 6a88feb docs: README와 제출 인덱스 정비
*   f8f9fd0 (origin/main, origin/HEAD, main, docs/ko-document-upddate) Merge pull request #28 from Codyssey-teamwork-B2-2-ko-park-chae/feature/chae-string-policy-edit
|\
| *   3df9461 (origin/feature/chae-string-policy-edit) Merge branch 'main' into feature/chae-string-policy-edit
| |\
| |/
|/|
* |   14c0463 Merge pull request #26 from Codyssey-teamwork-B2-2-ko-park-chae/feature/ko-string-policy-tabs
|\ \
| * | 9547205 (origin/feature/ko-string-policy-tabs, feature/ko-string/policy-tabs) docs: 문자열 정책을 스페이스·탭 제거로 변경
* | | 815eea9 Merge pull request #24 from Codyssey-teamwork-B2-2-ko-park-chae/feature/ko-string-policy-move
|\| |
```

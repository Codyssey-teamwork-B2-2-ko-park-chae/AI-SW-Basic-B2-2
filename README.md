# 🛠️ Team Python Utility Toolkit (AI-SW-Basic-B2-2)

고준석·채민성·박영세가 GitHub Flow, Issue–PR 연동, 코드 리뷰, 충돌 해결 및 Git 트러블슈팅을 연습하며 만든 Python 유틸리티 라이브러리입니다. 수학·문자열·날짜 모듈의 공개 함수 13개와 단위 테스트 22개를 포함합니다.

**최신화 기준: 2026-10-01 (한국 시간).** 원격 협업 이력은 [PR #28 병합 커밋 `f8f9fd0`](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/commit/f8f9fd0687c2d6405408ba7c8d01f5acb5ed7f33)까지 확인했습니다. 구현·테스트 설명은 현재 작업 폴더의 코드를 기준으로 작성했습니다. 제출 증빙과 보완 항목은 [SUBMISSION.md](SUBMISSION.md)에 정리합니다.

## 📌 GitHub Flow 채택 이유

1. `main`과 작업 브랜치 중심으로 변경 흐름을 단순하게 유지합니다.
2. Issue와 PR로 작업 목적을 연결하고, 팀원 리뷰와 테스트 결과를 확인한 뒤 병합합니다.
3. 작은 단위로 변경을 공유하여 충돌과 피드백을 빠르게 처리합니다.

협업 규칙은 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)를 따릅니다. `main`에는 PR 및 승인 1명 요건이 설정되어 있으며, 테스트 통과는 팀 협업 규칙입니다. 현재 GitHub Actions 워크플로와 필수 상태 검사 설정은 없습니다. 상세 규칙과 예외는 [제출 인덱스](SUBMISSION.md#5-브랜치-보호-규칙-증빙)를 참고합니다.

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

`strip_all_whitespace()`는 현재 ASCII 스페이스(`" "`)만 제거하고 탭·줄바꿈은 유지합니다. 원격 `main`의 [최종 정책 문서](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/blob/f8f9fd0687c2d6405408ba7c8d01f5acb5ed7f33/utils/string-policy.md)는 스페이스·탭·줄바꿈 제거를 명시하므로 구현 및 테스트 보완이 필요합니다. 현재 작업 브랜치의 [utils/string-policy.md](utils/string-policy.md)는 PR #26의 스페이스·탭 정책 시점에 있습니다.

날짜 파싱(`parse_date_string`)과 상대 시간 계산(`get_relative_time_string`)은 구현되어 있지 않습니다. 상대 시간 작업은 WIP 주석만 있으며 [Issue #15](https://github.com/Codyssey-teamwork-B2-2-ko-park-chae/AI-SW-Basic-B2-2/issues/15)는 확인 시점에 열려 있습니다.

## 💻 개발 및 테스트

- 권장 환경: Python 3.12. 이번 검증은 Python **3.12.14**, pytest **9.1.1**로 실행했습니다.
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

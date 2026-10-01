# Python 가상환경과 pytest 설정

권장 환경은 Python 3.12입니다. 저장소 루트에서 실행해야 `src.utils` import와 `tests/` 경로가 맞습니다. 별도 패키지 설정 파일이 없으므로 실행 코드 설치 과정은 필요하지 않으며, 테스트용 `pytest`만 설치합니다.

## macOS / Ubuntu

Python 3.12가 설치되어 있다고 가정합니다. `python3`가 원하는 버전을 가리킨다면 아래 `python3.12` 대신 사용할 수 있습니다. 먼저 `python3 --version`으로 확인합니다.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
python -m pytest tests/ -v
```

Ubuntu에서 가상환경 생성 시 `ensurepip` 오류가 발생하고 Python 3.12를 apt로 설치했다면, 해당 버전의 가상환경 패키지를 설치한 뒤 다시 생성합니다.

```bash
sudo apt update
sudo apt install python3.12-venv
python3.12 -m venv .venv
```

Python 버전과 Ubuntu 저장소 구성에 따라 패키지 이름·제공 여부가 달라질 수 있습니다.

## Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest
python -m pytest tests/ -v
```

활성화가 실행 정책에 의해 제한되면 가상환경의 Python을 직접 실행할 수 있습니다.

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest tests/ -v
```

## 재사용 및 종료

이미 `.venv`를 만들었다면 다음 작업부터는 운영체제에 맞는 활성화 명령부터 실행합니다. 사용 중인 환경은 다음 명령으로 확인합니다.

```bash
python --version
python -m pip --version
python -m pytest --version
```

캐시 파일 없이 간단히 검증하려면 다음 명령을 사용합니다.

```bash
python -m pytest tests/ -q -p no:cacheprovider
```

현재 테스트는 수학 7개, 문자열 9개, 날짜 6개로 총 22개입니다. 기존 문자열 테스트는 스페이스 제거만 확인하며 탭·줄바꿈 제거는 검증하지 않습니다.

가상환경을 종료할 때는 `deactivate`를 실행합니다. 프로젝트 소개와 실제 API는 [README](../../README.md), 테스트 결과 및 증빙 범위는 [제출 인덱스](../../SUBMISSION.md)를 참고합니다.

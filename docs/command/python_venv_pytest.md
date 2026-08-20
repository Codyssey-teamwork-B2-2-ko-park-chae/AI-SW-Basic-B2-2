# Python 3.12 가상환경과 pytest 설정

Ubuntu에서 Python 3.12 가상환경을 만들고 `pytest`를 설치하는 순서는 다음과 같습니다.

```bash
# 1. Python 3.12 가상환경 기능 설치
sudo apt install python3.12-venv

# 2. 가상환경 생성
python3.12 -m venv .venv

# 3. 가상환경 활성화
source .venv/bin/activate

# 4. pip 업데이트 및 pytest 설치
python -m pip install --upgrade pip
python -m pip install pytest

# 5. 테스트 실행
python -m pytest
```

가상환경을 종료하려면 다음 명령어를 실행합니다.

```bash
deactivate
```

이미 `.venv`를 생성했다면 다음부터는 가상환경 활성화 단계부터 실행하면 됩니다.

```bash
source .venv/bin/activate
```

# GitHub Issue 생성 명령어

GitHub CLI(`gh`)로 이슈를 생성하는 명령어입니다.

```bash
gh issue create --title "이슈 제목" --body "이슈 내용"
```

## 대화형으로 작성하기

```bash
gh issue create
```

## 특정 저장소에 생성하기

```bash
gh issue create --repo OWNER/REPOSITORY --title "이슈 제목" --body "이슈 내용"
```

## 여러 줄로 이슈 내용 작성하기

`--body-file -`와 heredoc을 사용하면 여러 줄의 내용을 그대로 입력할 수 있습니다.

```bash
gh issue create --title "로그인 오류 수정" --body-file - <<'EOF'
## 문제

로그인 버튼을 클릭해도 화면이 전환되지 않습니다.

## 재현 방법

1. 로그인 페이지로 이동합니다.
2. 이메일과 비밀번호를 입력합니다.
3. 로그인 버튼을 클릭합니다.

## 기대 결과

로그인 후 메인 화면으로 이동해야 합니다.
EOF
```

## GitHub CLI 로그인

로그인이 되어 있지 않다면 먼저 다음 명령어를 실행합니다.

```bash
gh auth login
```

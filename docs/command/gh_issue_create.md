# GitHub Issue 생성 명령어

GitHub CLI(`gh`)로 이슈를 생성하는 명령어입니다.

`gh`가 설치된 환경에서 저장소 루트로 이동하여 실행합니다. 로그인 상태는 `gh auth status`로 확인하며, 저장소의 [기능 요청 템플릿](../../.github/ISSUE_TEMPLATE/feature_request.md)을 참고해 목표·세부 작업·검증 기준을 작성합니다. 생성된 이슈 번호는 PR 본문에 `Closes #<이슈번호>` 또는 `Fixes #<이슈번호>`로 연결합니다. [협업 가이드](../CONTRIBUTING.md)

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

`--body-file -`와 heredoc을 사용하면 여러 줄의 내용을 그대로 입력할 수 있습니다. 아래는 작성 형식 예시이며, 제목과 내용은 실제 유틸리티 작업에 맞게 바꿉니다. [GitHub CLI 공식 문서](https://cli.github.com/manual/gh_issue_create)

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

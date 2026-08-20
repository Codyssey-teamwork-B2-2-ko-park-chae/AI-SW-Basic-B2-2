# `gh pr create`

이 문서는 [협업 가이드](../CONTRIBUTING.md)의 규칙에 맞춰 GitHub CLI로 PR을 생성하는 방법을 설명한다.

## PR 생성 전 확인

- PR의 대상 브랜치는 `main`으로 지정한다. `main`에는 직접 push하지 않는다.
- 작업 브랜치는 `<type>/<member_name>-<feature-name>` 형식을 사용한다.
  - 예: `feature/kim-login`, `refactor/kim-package-structure`, `fix/lee-strip-edge-case`
- PR 본문 첫 줄에는 `Closes #<이슈번호>` 또는 `Fixes #<이슈번호>`를 작성한다.
- 본문은 변경 사항(What), 변경 이유(Why), 테스트 및 검증 방법(How)을 포함한다.
- PR을 생성하기 전에 로컬 테스트가 모두 통과하는지 확인한다.

```bash
pytest
git push -u origin feature/kim-login
```

## 한 줄 명령어

다음 예시는 Bash의 `$'...'` 문자열을 사용해 본문의 줄바꿈을 표현한다.

```bash
gh pr create --base main --head feature/kim-login --title "feat: 로그인 기능 추가" --body $'Closes #123\n\n## 변경 사항 (What)\n- 로그인 기능을 추가했습니다.\n\n## 변경 이유 및 배경 (Why)\n- 사용자 인증이 필요합니다.\n\n## 테스트 및 검증 방법 (How)\n- [x] 로컬 단위 테스트 실행 (`pytest`)\n- [x] 주요 엣지 케이스 검증\n- [x] `main` 브랜치와 충돌 여부 확인\n\n## 리뷰어에게 요청할 점 (Notes for Reviewer)\n- 인증 실패 처리 방식을 중점적으로 확인해 주세요.'
```

## 여러 줄 명령어

```bash
gh pr create \
  --base main \
  --head feature/kim-login \
  --title "feat: 로그인 기능 추가" \
  --body "$(cat <<'EOF'
Closes #123

## 변경 사항 (What)
- 로그인 기능을 추가했습니다.

## 변경 이유 및 배경 (Why)
- 사용자 인증이 필요합니다.

## 테스트 및 검증 방법 (How)
- [x] 로컬 단위 테스트 실행 (`pytest`)
- [x] 주요 엣지 케이스 검증
- [x] `main` 브랜치와 충돌 여부 확인

## 리뷰어에게 요청할 점 (Notes for Reviewer)
- 인증 실패 처리 방식을 중점적으로 확인해 주세요.
EOF
)"
```

## `--fill`로 커밋 정보 사용하기

현재 브랜치의 커밋 정보로 PR 제목과 본문을 자동 작성하려면 `--fill`을 사용한다.

```bash
gh pr create --base main --head feature/kim-login --fill
```

예를 들어 최근 커밋 메시지가 다음과 같다면,

```text
feat: 로그인 기능 추가

JWT 기반 로그인 API를 구현했습니다.
```

다음과 같은 제목과 본문으로 PR이 생성된다.

```text
제목: feat: 로그인 기능 추가
본문: JWT 기반 로그인 API를 구현했습니다.
```

`--fill`은 커밋 메시지로 제목과 본문을 채울 뿐, 필수 이슈 연결과 What/Why/How 구조를 자동으로 보장하지 않는다. 다음처럼 편집기를 열어 본문 첫 줄과 필수 항목을 확인하고 보완한다.

```bash
gh pr create --base main --head feature/kim-login --fill --editor
```

PR 생성에 성공하면 터미널에는 다음과 비슷한 결과가 출력된다.

```text
Creating pull request for feature/kim-login into main in octocat/my-app

https://github.com/octocat/my-app/pull/42
```

## 생성 후 병합 요건

- 최소 1명 이상의 팀원 승인을 받는다.
- 로컬 테스트(`pytest`)가 모두 통과했는지 확인한다.
- 미해결된 Review Conversation이 없어야 한다.
- 모든 요건을 충족한 뒤 PR을 통해 `main`에 병합한다.

## PR 템플릿 경로 참고

협업 가이드는 PR 템플릿 경로를 `.github/pull_request_template.md`로 안내하지만, 현재 저장소의 템플릿 파일은 `.github/ISSUE_TEMPLATE/pull_request_template.md`에 있다. 자동 PR 템플릿을 사용하려면 파일 경로와 본문 첫 줄 규칙을 협업 가이드에 맞게 정리해야 한다. 위 명령어 예시는 경로가 정리되기 전에도 규칙을 지킬 수 있도록 본문을 직접 지정한다.

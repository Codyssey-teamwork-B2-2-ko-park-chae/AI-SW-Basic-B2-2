# GitHub PR 생성 명령어

[협업 가이드](../CONTRIBUTING.md)에 맞춰 저장소 루트에서 실행합니다. GitHub CLI(`gh`)가 설치되어 있어야 하며, 로그인 상태는 `gh auth status`로 확인합니다. 필요하면 `gh auth login`으로 로그인합니다.

## 생성 전 확인

- 작업 브랜치는 `<type>/<member_name>-<feature-name>` 형식을 사용합니다. 예: `feature/chae-advanced-strings`, `refactor/ko-package-structure`, `fix/chae-strip-whitespace`.
- `main`을 대상으로 PR을 만들고, 본문에는 실제 이슈 번호로 `Closes #<이슈번호>` 또는 `Fixes #<이슈번호>`를 작성합니다.
- [PR 템플릿](../../.github/pull_request_template.md)의 연결 이슈, What / Why / How, 리뷰 요청 항목을 포함합니다.
- 검증 체크박스는 직접 수행한 항목만 체크합니다.

```bash
python -m pytest tests/ -q
git push -u origin feature/chae-advanced-strings
```

## 본문을 직접 지정하기

아래 브랜치와 이슈 번호는 예시입니다. 실제 작업 브랜치·이슈로 바꿔 실행합니다. `--body-file -`는 표준 입력에서 본문을 읽으므로 줄바꿈을 그대로 전달할 수 있습니다. [GitHub CLI 공식 문서](https://cli.github.com/manual/gh_pr_create)

```bash
gh pr create \
  --base main \
  --head feature/chae-advanced-strings \
  --title "feat: 문자열 슬러그와 단어 축약 기능 추가" \
  --body-file - <<'EOF'
Closes #18

## 연결 이슈 (Linked Issue)
- #18

## 변경 사항 (What)
- 문자열 슬러그 변환과 단어 수 기준 축약 기능을 추가했습니다.

## 변경 이유 및 배경 (Why)
- 문자열 처리 유틸리티의 사용 범위를 확장합니다.

## 테스트 및 검증 방법 (How)
- [ ] 로컬 단위 테스트 실행 (`python -m pytest tests/ -q`)
- [ ] 빈 문자열 및 단어 수 경계 사례 검증
- [ ] main 브랜치와 충돌 여부 확인

## 리뷰어에게 요청할 점 (Notes for Reviewer)
- 문자열 변환 규칙과 접미사 처리 방식을 확인해 주세요.
EOF
```

## 템플릿 또는 커밋 정보로 작성하기

템플릿을 편집기로 열어 작성하려면 다음 명령을 사용합니다.

```bash
gh pr create --base main --template .github/pull_request_template.md --editor
```

현재 브랜치의 커밋 정보로 제목과 본문을 채우려면 `--fill`을 사용합니다. 여러 커밋이 있으면 결과가 달라질 수 있으며, 이슈 연결과 What / Why / How 구조를 자동으로 보장하지 않습니다. 편집기에서 해당 항목을 보완합니다.

```bash
gh pr create --base main --fill --editor
```

생성에 성공하면 PR URL이 출력됩니다. 최소 1명의 팀원 승인, 로컬 테스트 통과, 미해결 리뷰 코멘트 해소를 확인한 뒤 병합합니다. 마지막 두 항목은 팀 운영 기준이며 서버에서 자동으로 강제하는 설정과 구분합니다.

## 템플릿 경로

현재 PR 템플릿은 `.github/pull_request_template.md`입니다. 과거 경로인 `.github/ISSUE_TEMPLATE/pull_request_template.md`로 안내하지 않습니다. 템플릿의 `Closes #<issue_number>` 자리표시자를 실제 이슈 번호로 바꾸고, YAML 메타데이터를 PR 본문에 그대로 남기지 않도록 확인합니다.

---
name: pull_request_template
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

## 연결 이슈 (Linked Issue)
- Closes #<issue_number>

---

## 변경 사항 (What)
- 어떤 기능/수정이 이루어졌는지 구체적으로 설명합니다.
- 예: `math_ops.py`에 `calculate_average`, `safe_divide` 함수 추가 및 예외 처리 구현

## 변경 이유 및 배경 (Why)
- 이 변경이 왜 필요한지, 어떤 문제를 해결하는지 작성합니다.
- 예: 0으로 나누는 연산 시 발생하는 ZeroDivisionError를 방지하고 기본값을 반환하도록 안정성 확보

## 테스트 및 검증 방법 (How)
- [ ] 로컬 단위 테스트 실행 (`pytest`)
- [ ] 엣지 케이스(예: 빈 리스트, 음수 입력 등) 동작 검증
- [ ] 브랜치 충돌 여부 사전 확인 (`git merge main` / rebase)

---

## 리뷰어에게 요청할 점 (Notes for Reviewer)
- 코드 리뷰 시 특별히 확인받고 싶은 부분이나 설계 상의 고민을 적어주세요.

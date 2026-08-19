def normalize_whitespace(text: str) -> str:
    """연속된 공백, 탭, 줄바꿈을 한 칸의 공백으로 정리한다."""
    return " ".join(text.split())


def count_words(text: str) -> int:
    """문자열에 포함된 단어 개수를 반환한다."""
    normalized = normalize_whitespace(text)

    if not normalized:
        return 0

    return len(normalized.split(" "))
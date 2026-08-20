"""문자열 처리 유틸리티 함수 모듈."""

def capitalize_words(text: str) -> str:
    """각 단어의 첫 글자를 대문자로 변환합니다."""
    return " ".join(word.capitalize() for word in text.split(" ")) if text else ""

def reverse_string(text: str) -> str:
    """문자열을 반전합니다."""
    return text[::-1]

def strip_all_whitespace(text: str) -> str:
    """모든 공백을 제거합니다."""
    return text.replace(" ", "") if text else ""
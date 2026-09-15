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

import re

def slugify(text: str) -> str:
    """URL 친화적인 slug 문자열로 변환합니다."""
    if not text:
        return ""
    text = re.sub(r"[^\w\s-]", "", text.lower().strip())
    return re.sub(r"[\s_-]+", "-", text).strip("-")

def truncate_words(text: str, max_words: int, suffix: str = "...") -> str:
    """지정된 단어 수를 초과하는 문자열을 축약합니다."""
    words = text.split()
    return " ".join(words[:max_words]) + suffix if len(words) > max_words else text

from src.utils.string_ops import count_words, normalize_whitespace


def test_normalize_whitespace() -> None:
    result = normalize_whitespace("hello   python")
    assert result == "hello python"


def test_normalize_whitespace_with_tab_and_newline() -> None:
    result = normalize_whitespace("hello\tpython\nworld")
    assert result == "hello python world"


def test_normalize_whitespace_with_empty_text() -> None:
    assert normalize_whitespace("") == ""
    assert normalize_whitespace("   ") == ""


def test_count_words() -> None:
    assert count_words("hello python world") == 3


def test_count_words_with_empty_text() -> None:
    assert count_words("") == 0
    assert count_words("   ") == 0
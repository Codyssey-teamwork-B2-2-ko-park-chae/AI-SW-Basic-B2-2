import pytest
from src.utils.string_ops import (
    capitalize_words,
    reverse_string,
    slugify,
    strip_all_whitespace,
    truncate_words,
)

def test_string_functions_with_empty_string():
    assert capitalize_words("") == ""
    assert reverse_string("") == ""
    assert strip_all_whitespace("") == ""
    assert slugify("") == ""


def test_reverse_string_with_korean_text():
    assert reverse_string("안녕하세요") == "요세하녕안"


def test_slugify_removes_punctuation():
    assert slugify(" Hello, World! ") == "hello-world"


def test_truncate_words():
    assert truncate_words("one two three", 2) == "one two..."


def test_truncate_words_with_custom_suffix():
    assert truncate_words("one two three", 2, suffix="~") == "one two~"


def test_truncate_words_within_limit():
    assert truncate_words("one two", 2) == "one two"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_strip_all_whitespace():
    assert strip_all_whitespace(" h e l l o ") == "hello"

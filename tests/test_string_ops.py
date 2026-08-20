import pytest
from src.string_ops import capitalize_words, reverse_string, strip_all_whitespace

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_strip_all_whitespace():
    assert strip_all_whitespace(" h e l l o ") == "hello"
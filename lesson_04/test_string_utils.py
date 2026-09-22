import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ===== Тесты для capitalize =====

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("скайп", "Скайп"),
    ("привет, мир", "Привет, мир"),
    ("питон", "Питон"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# ===== Тесты для trim =====

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   скайп", "скайп"),
    ("  питон", "питон"),
    (" тест ", "тест "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "  "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# ===== Тесты для contains =====

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "y", True),
    ("SkyPro", "Pro", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("SkyPro", "", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# ===== Тесты для delete_symbol =====

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", "o", "Hell Wrld"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", "SkyPro"),
    ("", "a", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
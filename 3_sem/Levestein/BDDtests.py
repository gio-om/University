from main import levenshtein_distance
import pytest


def test_equal():
    assert levenshtein_distance("Валера", "Валера") == 0


def test_diff():
    assert levenshtein_distance("Разведка", "Разводка") == 1


def test_empty():
    assert levenshtein_distance("", "Привет") == 6


if __name__ == '__main__':
    pytest.main()

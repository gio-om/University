import unittest
from main import levenshtein_distance


class TestLevenshteinDistance(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(levenshtein_distance("Валера", "Валера"), 0)

    def test_diff(self):
        self.assertEqual(levenshtein_distance("Разведка", "Разводка"), 1)

    def test_empty(self):
        self.assertEqual(levenshtein_distance("", "Привет"), 6)


if __name__ == '__main__':
    unittest.main()

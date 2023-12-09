import unittest
from main import *


# Тестирование класса "Студент"
class TestStudent(unittest.TestCase):

    def test_student_creation(self):
        student = Student(1, "Беляев", 2, 4.5)
        self.assertEqual(student.student_id, 1)
        self.assertEqual(student.name, "Беляев")
        self.assertEqual(student.class_id, 2)
        self.assertEqual(student.avg_rating, 4.5)


# Тестирование класса "Класс"
class TestClass(unittest.TestCase):

    def test_computer_classroom_creation(self):
        cls = Class(1, "1Б")
        self.assertEqual(cls.class_id, 1)
        self.assertEqual(cls.name, "1Б")


# Тестирование выполнения запросов
class TestQueryExecution(unittest.TestCase):
    def setUp(self):
        self.classes, self.students, self.student_class = generate_data()

    # Тестирование запроса №1
    def test_query1(self):
        result = query1(self.student_class)
        self.assertEqual(result, [("Абрамов", "10А")])

    # Тестирование запроса №2
    def test_query2(self):
        result = query2(self.student_class)
        self.assertEqual(result, [("10А", 2.7), ("2Б", 3.8), ("5В", 5.0)])

    # Тестирование запроса №3
    def test_query3(self):
        result = query3(self.student_class)
        self.assertEqual(result,
                         [("Абрамов", "10А"), ("Барсукова", "5В"), ("Гукасян", "2Б"),
                          ("Иноземцев", "10А"), ("Лупарев", "2Б")])


if __name__ == "__main__":
    unittest.main()
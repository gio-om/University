class Student:
    def __init__(self, student_id: int, name: str, class_id: int, avg_rating: float):
        self._student_id = student_id
        self._name = name
        self._class_id = class_id
        self._avg_rating = avg_rating

    @property
    def student_id(self) -> int:
        return self._student_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def class_id(self) -> int:
        return self._class_id

    @property
    def avg_rating(self) -> float:
        return self._avg_rating


class Class:
    def __init__(self, class_id: int, name: str):
        self._class_id = class_id
        self._name = name

    @property
    def class_id(self) -> int:
        return self._class_id

    @property
    def name(self) -> str:
        return self._name


def query1(student_class: list):
    # Задание В1
    data = []
    for student, cls in student_class:
        if student.name.startswith('А'):
            data.append((student.name, cls.name))
    return data


def query2(student_class: list):
    # Задание В2
    data = []
    class_min_ratings = {}
    for student, cls in student_class:
        if cls.name in class_min_ratings:
            if student.avg_rating < class_min_ratings[cls.name]:
                class_min_ratings[cls.name] = student.avg_rating
        else:
            class_min_ratings[cls.name] = student.avg_rating

    sorted_classes = sorted(class_min_ratings.items(), key=lambda x: x[1])
    for group, min_rating in sorted_classes:
        data.append((group, min_rating))
    return data


def query3(student_class: list):
    # Задание В3
    data = []
    student_class.sort(key=lambda x: x[0].name)
    for student, cls in student_class:
        data.append((student.name, cls.name))
    return data


def generate_data():
    # Создаем объекты класса Class
    classes = [
        Class(1, "2Б"),
        Class(2, "10А"),
        Class(3, "5В")
    ]

    # Создаем объекты класса Student
    students = [
        Student(1, "Лупарев", 1, 4.9),
        Student(2, "Гукасян", 1, 3.8),
        Student(3, "Абрамов", 2, 4.5),
        Student(4, "Иноземцев", 2, 2.7),
        Student(5, "Барсукова", 3, 5.0)
    ]

    # Создаем список "Школьникик и классы" для связи один-ко-многим
    student_class = [
        (students[0], classes[0]),
        (students[1], classes[0]),
        (students[2], classes[1]),
        (students[3], classes[1]),
        (students[4], classes[2])
    ]
    return classes, students, student_class


def execute_queries(student_class: list):
    print("Задание В1")
    for stud, cls in query1(student_class):
        print(f"{stud} - {cls}")
    print()

    print("Задание В2")
    for group, rating in query2(student_class):
        print(f"{group} - Минимальный рейтинг: {rating}")
    print()

    print("Задание В3")
    for stud, cls in query3(student_class):
        print(f"{stud} - {cls}")
    print()


def main():
    # Генерация данных
    classes, students, student_class = generate_data()

    # Запуск запросов
    execute_queries(student_class)


if __name__ == '__main__':
    main()
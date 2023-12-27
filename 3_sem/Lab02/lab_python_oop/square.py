from lab_python_oop.color import Color
from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_, color_):
        self.side = side_
        self.my_color = Color(color_)
        self.name = "Квадрат"

    def area(self):
        return self.side * self.side

    def get_name(self):
        return self.name

    def __repr__(self):
        return "Фигура: {}, Длина стороны - {}, Цвет - {}, Площадь - {}".format(self.get_name(), self.side,
                                                                                     self.my_color.color, self.area())

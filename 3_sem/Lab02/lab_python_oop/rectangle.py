from lab_python_oop.color import Color
from lab_python_oop.geom_figure import Figure


class Rectangle(Figure):
    def __init__(self, length_, width_, color_):
        self.length = length_
        self.width = width_
        self.my_color = Color(color_)
        self.name = "Прямоугольник"

    def area(self):
        return self.width * self.length

    def get_name(self):
        return self.name

    def repr(self):
        return "Фигура: {}, Длина - {}, Ширина - {}, Цвет - {}, Площадь - {}".format(self.get_name(),
                                                                                          self.length,
                                                                                          self.width,
                                                                                          self.my_color.color,
                                                                                          self.area())

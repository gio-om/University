import numpy as np

from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square


def main():
   # rectangle = Rectangle(5, 10, "Biege")
    #print(rectangle.repr())
    #circle = Circle(10, "Black")
    #print(circle)
    square = Square(4, "Cyan")
    print(square)
    matrix = np.array(([10, 15, 9],
                     [5, 7, 1]))
    print(matrix)


if __name__ == "__main__":
    main()

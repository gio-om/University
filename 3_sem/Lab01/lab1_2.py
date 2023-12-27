import sys
import math

class SquareRoots:
    def __init__(self):
        '''
        Конструктор класса
        '''
        self.coef_A = None
        self.coef_B = None
        self.coef_C = None
        self.num_roots = 0
        self.roots_list = []

    def get_coef(self, index, prompt):
        '''
        Читаем коэффициент из командной строки или вводим с клавиатуры
        Args:
            index (int): Номер параметра в командной строке
            prompt (str): Приглашение для ввода коэффицента
        Returns:
            float: Коэффициент квадратного уравнения
        '''
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()

        try:
            coef = float(coef_str)
            if coef == 0 and index == 1:
                print("Введите не 0")
                return self.get_coef(index, prompt)
            return coef
        except:
            print("Введите число")
            return self.get_coef(index, prompt)

    def get_coefs(self):
        '''
        Чтение трех коэффициентов
        '''
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        '''
        Вычисление корней квадратного уравнения
        '''
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        D = b*b - 4*a*c
        if D == 0.0:
            root = -b / (2.0*a)
            self.num_roots = 1
            self.roots_list.append(root)
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0*a)
            root2 = (-b - sqD) / (2.0*a)
            if root1 >= 0:
                self.num_roots += 2
                self.roots_list.append(math.sqrt(root1))
                self.roots_list.append((-1) * math.sqrt(root1))
            if root2 >= 0:
                self.num_roots += 2
                self.roots_list.append(math.sqrt(root2))
                self.roots_list.append((-1) * math.sqrt(root2))

    def print_roots(self):
        if self.num_roots != len(self.roots_list):
            print(('Ошибка. Уравнение содержит {} действительных корней, ' +\
                'но было вычислено {} корней.').format(self.num_roots, len(self.roots_list)))
        else:
            if self.num_roots == 0:
                print('Нет корней')
            elif self.num_roots == 2:
                print('Два корня: {} и {}'.format(self.roots_list[0], self.roots_list[1]))
            elif self.num_roots == 2:
                print('Четыре корня: {}; {}; {}; {}'.format(self.roots_list[0], self.roots_list[1],
                                                  self.roots_list[2], self.roots_list[3]))


def main():
    '''
    Основная функция
    '''
    r = SquareRoots()

    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

if __name__ == "__main__":
    main()


import sys
import math


def get_coef(index, prompt):
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
            return get_coef(index, prompt)
        return coef
    except:
        print("Введите число")
        return get_coef(index, prompt)


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 >= 0:
            result.append(math.sqrt(root1))
            result.append((-1) * math.sqrt(root1))
        if root2 >= 0:
            result.append(math.sqrt(root2))
            result.append((-1) * math.sqrt(root2))
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)

    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 2:
        print('Четыре корня: {}; {}; {}; {}'.format(roots[0], roots[1], roots[2], roots[3]))

    print('Press Enter to exit')
    end = input()

if __name__ == "__main__":
    main()


import math


def integral(left_b, right_b, flag_func):
    # задаём точность вычислений, на сколько частей будем делить интервал
    n = 1000000

    # текущее значение переменной для функции
    # на старте оно совпадает с первой границей
    current = left_b

    # функция, которую нужно проингтегрировать
    def integration(x, flag_func):
        match flag_func:
            case 0:
                return math.sin(x) + math.cos(x)
            case 1:
                return x ** 2
            case 2:
                return math.sin(2 * x)

    # считаем шаг интегрирования, оно же — ширина мини-прямоугольника
    h = (right_b - left_b) / n

    # здесь будем хранить значение получившегося интеграла
    s = 0
    # пока не дошли до другой границы — цикл работает
    while current <= right_b:
        # находим значение функции в текущей точке и умножаем его на значение шага
        # так мы получим площадь очень маленького прямоугольника, который можно нарисовать в этой точке
        # общая площадь фигуры — это сумма всех таких маленьких прямоугольников
        s += ((integration(current, flag_func)) * h)
        # сдвигаемся к следующей точке
        current += h

    return s


if __name__ == '__main__':
    # задаём границы интегрирования
    # считать будем от -1 до пи
    left = -1
    right = math.pi
    for flag in range(3):
        if flag == 0:
            f = 'sin(x) + cos(x)'
        elif flag == 1:
            f = 'x^2'
        else:
            f = 'sin2x'
        print(f"Площадь функции {f} в пределах от {left} до pi")
        square = integral(left, right, flag)

        # если интеграл получился отрицательный
        if square < 0:
            square = abs(square)
        print("равна: ", square)

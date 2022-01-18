import random

"""Здесь запоминаем уже посчитанные порядковые значения Фибоначчи"""
known = {0: 0, 1: 1}


def fibonacci(n):
    """Если уже посчитано, то возьмём из словаря"""
    if n in known:
        """Базовый случай"""
        return known[n]
    """Рекурсия только по новому делу"""
    res = fibonacci(n - 1) + fibonacci(n - 2)
    """Запишем новое значение в словарь"""
    known[n] = res
    return res


if __name__ == '__main__':
    """Тест"""
    for i in range(1):
        num = random.randint(1, 16)
        print(num, '- число Фибоначчи это', fibonacci(num))

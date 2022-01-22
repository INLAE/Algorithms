import random

"""Здесь запоминаем уже посчитанные значения Факториала"""
known = {0: 0, 1: 1}


def factorial(n):
    """Если уже посчитано, то возьмём из словаря"""
    if n in known:
        """Базовый случай"""
        return known[n]
    else:
        """Рекурсия, если ранее не считали"""
        res = n * factorial(n - 1)
        """Добавляем в словарь"""
        known[n] = res
        return res


if __name__ == '__main__':
    """Тест"""
for i in range(3):
    n = random.randint(1, 10)
    """f-строка"""
    print(f'Факториал {n} -', factorial(n))

print(known)

import random

"""Евклидов алгоритм для нахождения наибольшего общего делителя двух чисел"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return ((a * b) // gcd(a, b))


if __name__ == '__main__':
    """Тест"""
    for i in range(3):
        num1 = random.randint(1, 66)
        num2 = random.randint(1, 66)
        print(f"For {num1} and {num2} GCD is", gcd(num1, num2), "LCM is", lcm(num1, num2), "\n")

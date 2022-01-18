import random


def isPrime(num):
    if num < 3:
        return (True)
    elif num % 2 == 0:
        return (False)
    else:
        a = 2
        """ Малая теорема Ферма """
        if ((a ** (num - 1)) - 1) % num == 0:
            return (True)
        else:
            return (False)


if __name__ == '__main__':
    for i in range(6):
        num = random.randint(1, 666)
        print(num, isPrime(num))

import random as r


class Tridim:
    def __init__(self):
        self.mas = []

    def create_list(self, q):
        self.mas = [[[r.randint(-10, 10) for i in range(q)] for j in range(q)] for k in range(q)]

    def show_list(self):
        return self.mas

    def delete_elem(self, i, j, k):
        return self.mas[i][j].pop(k)

    def insert_elem(self, i, j, k, num):
        return self.mas[i][j].insert(k, num)

    def find_elem(self, num):
        for i in range(3):
            for j in range(3):
                for k in range(len(self.mas[i][j])):
                    if num == self.mas[i][j][k]:
                        return (i, j, k)


if __name__ == "__main__":
    t = Tridim()
    t.create_list(3)
    i = 0
    while i != 5:
        print('Выберите действие:')
        i = int(input('1. Просмотр 3-х мерного списка \n'
                      '2. Удаление элемента списка \n'
                      '3. Вставка элемента \n'
                      '4. Поиск элемента списка \n'
                      '5. Выход \n'))
        if i == 1:
            a = t.show_list()
            for i in range(3):
                print(a[i])
        elif i == 2:
            i, j, k = map(int, input('Введите адрес элемента [i][j][k]: ').split(' '))
            print(t.delete_elem(i, j, k))
        elif i == 3:
            i, j, k, num = map(int, input('Введите адрес элемента [i][j][k] и число: ').split(' '))
            t.insert_elem(i, j, k, num)
            a = t.show_list()
            for i in range(3):
                print(a[i])
        elif i == 4:
            num = int(input('Введите число для поиска: '))
            print('Адрес', num, 'по i j k --', t.find_elem(num))

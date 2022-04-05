import copy
import random as r


class avl:

    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        if self.left != None:
            if self.right != None:
                if self.left.height > self.right.height:
                    self.height = self.left.height + 1
                else:
                    self.height = self.right.height + 1
            else:
                self.height = self.left.height + 1
        elif self.right != None:
            self.height = self.right.height + 1
        else:
            self.height = 0

    def add(self, tree):
        if not isinstance(tree, avl):
            tree = avl(tree)
        if tree.value < self.value:
            if self.left != None:
                self.left.add(tree)
            else:
                self.left = tree
            self.left.parent = self
            if abs(self.calcHeight(self.left) - self.calcHeight(self.right)) >= 2:
                if self.calcHeight(self.left.left) >= self.calcHeight(self.left.right):
                    self.swap(self.rotateRight())
                else:
                    self.swap(self.doubleRight())
        else:
            if self.right != None:
                self.right.add(tree)
            else:
                self.right = tree
            self.right.parent = self
            if abs(self.calcHeight(self.left) - self.calcHeight(self.right)) >= 2:
                if self.calcHeight(self.right.right) >= self.calcHeight(self.right.left):
                    self.swap(self.rotateLeft())
                else:
                    self.swap(self.doubleLeft())
        self.height = self.calcHeight(self)
        return self

    def delete(self, element):
        if self.value == element:
            if self.left == None and self.right == None:
                self.value = None
            elif self.left != None and self.right == None:
                self.swap(self.left)
            elif self.right != None and self.left == None:
                self.swap(self.left.right)
            else:
                prec = copy.copy(self.predecesor(self.right))
                self.delete(prec.value)
                if self.right and self.right.value == None:
                    self.right = None
                self.value = prec.value
        elif self.value > element and self.left != None:
            self.left.delete(element)
            if self.left.value == None:
                self.left = None
        elif self.right != None:
            self.right.delete(element)
            if self.right.value == None:
                self.right = None
        if abs(self.calcHeight(self.left) - self.calcHeight(self.right)) >= 2:
            if self.value < element:
                a = self.calcHeight(self.left.right)
                b = self.calcHeight(self.left.left)
            else:
                a = self.calcHeight(self.right.left)
                b = self.calcHeight(self.right.right)
            if a <= b:
                if self.value > element:
                    self.swap(self.rotateLeft())
                else:
                    self.swap(self.rotateRight())
            else:
                if self.value > element:
                    self.swap(self.doubleLeft())
                else:
                    self.swap(self.doubleRight())
        self.height = self.calcHeight(self)
        return self

    def predecesor(self, element):
        if element.left != None:
            while element.left != None:
                element = element.left
        else:
            parent = element.parent
        return element

    def rotateLeft(self):
        temp = copy.copy(self.right)
        self.right = temp.left
        temp.left = copy.copy(self)
        temp.left.parent = temp

        if self.right:
            self.right.height = self.calcHeight(self.right)

        self.height = self.calcHeight(self)

        return temp

    def doubleLeft(self):
        temp = copy.copy(self.right.left)
        self.right.left = temp.right
        temp.right = copy.copy(self.right)
        temp.right.parent = temp
        self.right = copy.copy(temp)

        temp = copy.copy(self.right)
        self.right = temp.left
        temp.left = copy.copy(self)
        temp.left.parent = temp
        if self.left:
            self.left.height = self.calcHeight(self.left)
        if self.right:
            self.right.height = self.calcHeight(self.right)
        self.height = self.calcHeight(self)
        return temp

    def rotateRight(self):
        temp = copy.copy(self.left)
        self.left = temp.right
        temp.right = copy.copy(self)
        temp.right.parent = temp
        if self.left:
            self.left.height = self.calcHeight(self.left)
        self.height = self.calcHeight(self)
        return temp

    def doubleRight(self):
        temp = copy.copy(self.left.right)
        self.left.right = temp.left
        temp.left = copy.copy(self.left)
        temp.left.parent = temp
        self.left = copy.copy(temp)

        temp = copy.copy(self.left)
        self.left = temp.right
        temp.right = copy.copy(self)
        temp.right.parent = temp
        if self.left:
            self.left.height = self.calcHeight(self.left)
        if self.right:
            self.right.height = self.calcHeight(self.right)
        self.height = self.calcHeight(self)
        return temp

    def swap(self, node):
        self.parent = node.parent
        self.left = node.left
        self.right = node.right
        self.height = node.height
        self.value = node.value

    def calcHeight(self, node):
        if node == None:
            return 0
        else:
            return max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1

    def breadthfirst(self):
        queue = [(0, self)]
        i = 0
        while len(queue):
            el = queue[0][1]
            level = queue[0][0]
            queue = queue[1:]
            if el.left != None:
                queue.append((level + 1, el.left))
            if el.right != None:
                queue.append((level + 1, el.right))
            yield (level, el)

    def preorder(self):
        stack = [self]
        while len(stack):
            elem = stack.pop()
            yield elem.value
            if elem.right != None:
                stack.append(elem.right)
            if elem.left != None:
                stack.append(elem.left)

    def postorder(self):
        stack = []
        elem = self
        while len(stack) or elem != None:
            while elem != None:
                stack.append((elem, 0))
                elem = elem.left
            elem = stack.pop()
            if elem[1] == 0:
                stack.append((elem[0], 1))
                elem = elem[0].right
            else:
                yield elem[0].value
                elem = None

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    cnt = int(input("Size of List: "))
    num = r.randint(-10, 10)
    a = avl(num)
    for i in range(cnt - 1):
        num = r.randint(-10, 100)
        a.add(num)

    prev = -1
    print('Текущее сбалансированное дерево: ')
    for i in a.breadthfirst():
        if prev != i[0]:
            print("\n")
            prev = i[0]
        print("|", i[1], "|", end="")

    print("\n1. Прямой проход. \n2. Обратный проход.\n3. Удалить элемент\n4. Вставить элемент\n"
          "5. Сбалансировать дерево\n6. Выход")
    ch = None
    while ch != 6:
        ch = int(input())
        if ch == 1:
            print("Прямой проход: ")
            for i in a.preorder():
                print(i, end=" ")
            print()
        elif ch == 2:
            print("Обратный проход: ")
            for i in a.postorder():
                print(i, end=" ")
            print()
        elif ch == 3:
            dl = int(input('Удалить элемент: '))
            a.delete(dl)
            print("Элемент удалён. Сбалансируйте дерево (5). \n")
        elif ch == 4:
            dl = int(input('Вставить элемент: '))
            a.add(dl)
            print("Элемент вставлен. Сбалансируйте дерево (5).\n")
        elif ch == 5:
            prev = -1
            print('Текущее сбалансированное дерево: ')
            for i in a.breadthfirst():
                if prev != i[0]:
                    print("\n")
                    prev = i[0]
                print("|", i[1], "|", end="")
            print('\n')

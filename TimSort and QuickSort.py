import random


def TSort(arr):
    """Определение minrun длины подмассива"""

    def find_minrun(n):
        """станет 1 если среди сдвинутых битов будет хотя бы 1 ненулевой"""
        r = 0
        """Граница minrun длины подмассива"""
        MINIMUM = 32

        while n >= MINIMUM:
            """|= update"""
            r |= n & 1
            n >>= 1
        return n + r

    """Cортировка вставками, а она эффективна только на небольших массивах --
    подмассивах minrun"""

    def insertion_sort(array, left, right):
        for i in range(left + 1, right + 1):
            element = array[i]
            j = i - 1
            while element < array[j] and j >= left:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = element
        return array

    def merge(array, l, m, r):
        array_length1 = m - l + 1
        array_length2 = r - m
        left = []
        right = []
        for i in range(0, array_length1):
            left.append(array[l + i])
        for i in range(0, array_length2):
            right.append(array[m + 1 + i])

        i = 0
        j = 0
        k = l

        while j < array_length2 and i < array_length1:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < array_length1:
            array[k] = left[i]
            k += 1
            i += 1

        while j < array_length2:
            array[k] = right[j]
            k += 1
            j += 1

    def tim_sort(arr):
        n = len(arr)
        minrun = find_minrun(n)

        """Определяем конец подмассива и 
        сортируем вставкой"""
        for start in range(0, n, minrun):
            end = min(start + minrun - 1, n - 1)
            insertion_sort(arr, start, end)

        """Сортируем подмассивы слиянием"""
        size = minrun
        while size < n:

            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))
                merge(array, left, mid, right)

            size = 2 * size

    tim_sort(arr)
    return (arr)


def QuickSort(array):
    if len(array) < 2:
        "базовый случай, если 0 или 1 элемент в массиве"
        return array
    else:
        "рекурсивный случай"
        pivot = array[0]
        # подмассив элементов меньших первого
        less = [i for i in array[1:] if i <= pivot]
        # подмассив элементов меньших первого
        greater = [i for i in array[1:] if i > pivot]
        "метод разделяй и властвуй"
        return QuickSort(less) + [pivot] + QuickSort(greater)


if __name__ == '__main__':
    arr = []
    for i in range(13):
        x = random.randint(-66, 66)
        arr.append(x)
    print('Array:', arr)

    "Timsort" \
    "со сложностью O(n*logn) в среднем и худшем случае, O(n) в лучшем"
    "https://www.youtube.com/watch?v=NVIjHj-lrT4"
    print('Timsort:', TSort(arr))

    "QuickSort" \
    "со сложностью O(n*logn) в лучшем и среднем случае и O(n^2) в худшем"
    "https://www.youtube.com/watch?v=8hEyhs3OV1w"
    print('Quick Sort:', QuickSort(arr))

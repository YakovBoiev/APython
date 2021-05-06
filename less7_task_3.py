""""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
 Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
 которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

M = 5
test_array = [random.randint(-100, 100) for _ in range(2 * M + 1)]
print(test_array)

def insert_sort(array):
    for i in range(1, len(array)):
        spam = i
        for j in range(i - 1, -1, -1):
            if array[j] > array[spam]:
                array[j], array[spam] = array[spam], array[j]
                spam -= 1
            else:
                break
    return array

sort_array = insert_sort(test_array)
print(sort_array)
print(f'Медианна массива {sort_array[len(test_array) // 2]}')

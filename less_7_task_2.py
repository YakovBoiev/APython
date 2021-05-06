""""
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

SIZE = 9
EL_MIN = 0
EL_MAX = 49
test_array = [random.uniform(EL_MIN, EL_MAX) for _ in range(SIZE)]
print(test_array)

def merge(l_array, r_array):
    merge_array = []
    while len(l_array) and len(r_array):
        if l_array[0] <= r_array[0]:
            merge_array.append(l_array.pop(0))
        else:
            merge_array.append(r_array.pop(0))
    merge_array.extend(l_array)
    merge_array.extend(r_array)
    return merge_array


def split_sort(array):
    if len(array) <= 1:
        return array
    l_array, r_array = array[:len(array) // 2], array[len(array) // 2:]
    l_array = split_sort(l_array)
    r_array = split_sort(r_array)
    fin_array = merge(l_array, r_array)
    return fin_array

print(split_sort(test_array))

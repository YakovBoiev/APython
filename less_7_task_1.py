"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
 заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
 Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random


SIZE = 10
EL_MIN = -100
EL_MAX = 99

test_array = [random.randint(EL_MIN, EL_MAX) for _ in range(10)]
print(test_array)


def bubble_sorts(array):
    for n in range(1, len(array)):
        flag = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = False
        if flag:
            break
    return array


print(bubble_sorts(test_array))

"""
Определить, какое число в массиве встречается чаще всего
"""
import cProfile
import timeit
import random

def test_array(n):
    SIZE = n
    MIN_NUM = - 100
    MAX_NUM = 100
    test_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
    return test_array

test_array10 = test_array(10)
test_array100 = test_array(100)
test_array1000 = test_array(1000)


def max_count(test_array):
    list_numb = [test_array[0]]
    list_count = [1]
    for i in range(1, len(test_array)):
        for j in range(len(list_numb)):
            if list_numb[j] == test_array[i]:
                list_count[j] += 1
                break
        else:
            list_numb.append(test_array[i])
            list_count.append(1)
    index_max = 0
    max_list_count = list_count[0]
    for i in range(1, len(list_count)):
        if max_list_count < list_count[i]:
            max_list_count = list_count[i]
            index_max = i
    return list_numb[index_max]

print(timeit.timeit('max_count(test_array10)', number=1000, globals=globals()))   #  0.017286124
print(timeit.timeit('max_count(test_array100)', number=1000, globals=globals()))  #  0.576355135
print(timeit.timeit('max_count(test_array1000)', number=1000, globals=globals())) # 12.794915396

cProfile.run('max_count(test_array1000)')

"""
1405 function calls in 0.014 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.014    0.014 <string>:1(<module>)
        1    0.013    0.013    0.014    0.014 less_4_task_1.py:20(max_count)
        1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      400    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

def max_count1(array):
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    return num

print(timeit.timeit('max_count1(test_array10)', number=1000, globals=globals()))   #  0.013419208000000182
print(timeit.timeit('max_count1(test_array100)', number=1000, globals=globals()))  #  0.7183118430000004
print(timeit.timeit('max_count1(test_array1000)', number=1000, globals=globals())) # 75.855516198

cProfile.run('max_count1(test_array1000)')

"""1005 function calls in 0.074 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.074    0.074 <string>:1(<module>)
        1    0.074    0.074    0.074    0.074 less_4_task_1.py:45(max_count1)
        1    0.000    0.000    0.074    0.074 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
def max_count2(array):
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    if num is not None:
        return num

print(timeit.timeit('max_count2(test_array10)', number=1000, globals=globals()))   # 0.003920563999997739
print(timeit.timeit('max_count2(test_array100)', number=1000, globals=globals()))  # 0.03522489799999562
print(timeit.timeit('max_count2(test_array1000)', number=1000, globals=globals())) # 0.40023904100000607

cProfile.run('max_count2(test_array1000)')

"""
4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 less_4_task_1.py:65(max_count2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
"""
Вывод
Сложность max_count O(n log n)
Сложность max_count1 O(n**2)
Сложность max_count2 O(n)

Max_count2 оптимальный

"""





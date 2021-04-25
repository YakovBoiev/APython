import timeit
import cProfile
from math import sqrt


def prime_numb(i):
    prime_numb = 1
    numb = prime_numb + 1
    count = 0
    while count < i:
        for j in range(2, int(sqrt(numb)) + 1, 1):
            if numb % j == 0:
                numb += 1
                break
        else:
            prime_numb = numb
            numb += 1
            count += 1
    return prime_numb
print(timeit.timeit('prime_numb(10)', number=100, globals=globals()))     #  0.004933360999999997
print(timeit.timeit('prime_numb(100)', number=100, globals=globals()))    #  0.064080046
print(timeit.timeit('prime_numb(1000)', number=100, globals=globals()))   #  1.367593952
print(timeit.timeit('prime_numb(10000)', number=100, globals=globals()))  # 38.618810964

cProfile.run('prime_numb(1000)')
""""
7922 function calls in 0.019 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
        1    0.017    0.017    0.019    0.019 less_4_task_2.py:6(prime_numb)
        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
     7918    0.002    0.000    0.002    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

def prime_numb1(k):
    sieve = [i if i > 1 else 0 for i in range(0, k * 20)]
    for i in range(2, len(sieve)):
        if sieve[i] != 0:
            for j in range(i * 2, len(sieve), i):
                sieve[j] = 0
    count = 0
    for i in range(len(sieve)):
        if sieve[i] != 0:
            count += 1
            if count == k:
                return sieve[i]

print(timeit.timeit('prime_numb1(10)', number=100, globals=globals()))     #  0.009034931999998719
print(timeit.timeit('prime_numb1(100)', number=100, globals=globals()))    #  0.09806169000000153
print(timeit.timeit('prime_numb1(1000)', number=100, globals=globals()))   #  1.031521729000005
print(timeit.timeit('prime_numb1(10000)', number=100, globals=globals()))  # 12.407429852

в
cProfile.run('prime_numb1(1000)')
""""
269 function calls in 0.011 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.011    0.011 <string>:1(<module>)
        1    0.009    0.009    0.011    0.011 less_4_task_2.py:27(prime_numb1)
        1    0.002    0.002    0.002    0.002 less_4_task_2.py:28(<listcomp>)
        1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
     2264    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Вывод 
Сложность prime_numb -  O(n log n), prime_numb1  - O(n log n)
prime_numb1 'Решето Эротосфена' предпочтительней для поиска больших простых чисел, но требует выделения большей памяти
   

"""



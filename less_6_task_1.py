"""""
Посчитать cумму четных и нечетных цифры введенного натурального числа.
"""
import sys

def total_mem(obj):
    total = sys.getsizeof(obj)
    if type(obj) != str:
        try:
            for item in obj:
                total += sys.getsizeof(item)
        except TypeError:
            return total
    return total


numb = int(input('Введите натуральное число '))
evsumdig = 0
oddsumdig = 0
while True:
    if numb % 2 == 0:
        evsumdig += 1
    else:
        oddsumdig += 1
    if numb // 10 == 0:
        break
    else:
        numb = numb // 10
print(f'Количество четных цифр - {evsumdig}')
print(f'Количество нечетных цифр - {oddsumdig}')
print(f'Затрачено памяти - ', end="")
print(f'{total_mem(numb) + total_mem(evsumdig) + total_mem(oddsumdig)} байт')
"""
Введите натуральное число 1234567890
Количество четных цифр - 5
Количество нечетных цифр - 5
Затрачено памяти - 84 байт
"""

numb = input('Введите натуральное число ')
evsumdig = 0
oddsumdig = 0
for dig in numb:
    if int(dig) % 2 == 0:
        evsumdig += 1
    else:
        oddsumdig += 1
print(f'Количество четных цифр - {evsumdig}')
print(f'Количество нечетных цифр - {oddsumdig}')
print(f'Затрачено памяти - ', end="")
print(f'{total_mem(numb) + total_mem(evsumdig) + total_mem(oddsumdig) + total_mem(dig) + total_mem(int(dig))} байт')
"""
Введите натуральное число 1234567890
Количество четных цифр - 5
Количество нечетных цифр - 5
Затрачено памяти - 189 байт
"""

numb = list(map(int, input('Введите натуральное число ')))
even_lst = [dig for dig in numb if dig % 2 == 0]
oddsumdig = len(numb) - len(even_lst)
print(f'Количество четных цифр - {len(even_lst)}')
print(f'Количество нечетных цифр - {oddsumdig}')
print(f'Затрачено памяти - ', end="")
print(f'{total_mem(numb) + total_mem(even_lst) + total_mem(oddsumdig) + total_mem(dig)} байт')
"""
Введите натуральное число 1234567890
Количество четных цифр - 5
Количество нечетных цифр - 5
Затрачено памяти - 762 байт
"""







"""
СЛОЖЕНИЕ

Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections

transl_16_10 = collections.defaultdict(int)
for index, char in enumerate('0123456789ABCDEF'):
    transl_16_10[char] = index

transl_10_16 = collections.defaultdict(int)
for key, value in dict.items(transl_16_10):
    transl_10_16[value] = key


def input_numb():
    numb = collections.deque()
    for char in input("Введите число в 16 -oй системе ").upper():
        numb.append(char)
    return numb


def add_16(numb1, numb2):
    diff = len(numb1) - len(numb2)
    if diff > 0:
        for _ in range(diff):
            numb2.appendleft(0)
    else:
        for _ in range(-diff):
            numb1.appendleft(0)
    rezult_numb = collections.deque()
    egg = 0
    while len(numb1) > 0:
        spam = int(transl_16_10[numb1.pop()]) + int(transl_16_10[numb2.pop()]) + egg
        if spam > 15:
            spam = spam % 16
            egg = 1
        else:
            egg = 0
        rezult_numb.appendleft(transl_10_16[spam])
    if egg == 1:
        rezult_numb.appendleft(1)
    return rezult_numb


numb1 = input_numb()
numb2 = input_numb()
numb3 = add_16(numb1, numb2)
print('Результат сложения чисел = ', end="")
print(*numb3, sep='')

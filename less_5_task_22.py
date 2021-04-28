"""
УМНОЖЕНИЕ
В сроки до урока № 6 и разбора ДЗ
успел написать только умножение на однозначное число.

Жду разбора ДЗ

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


def mult_16(numb1, numb2):
    rezult_numb = collections.deque()
    egg = 0
    while len(numb2) > 0:
        spam2 = int(transl_16_10[numb2.pop()])
        while len(numb1) > 0:
            spam = int(transl_16_10[numb1.pop()]) * spam2 + egg
            if spam > 15:
                egg = spam // 16
                spam = spam % 16
            else:
                egg = 0
            rezult_numb.appendleft(transl_10_16[spam])
        if egg > 0:
            rezult_numb.appendleft(transl_10_16[egg])
    return rezult_numb


numb1 = input_numb()
numb2 = input_numb() # Tолько однозначное число!!!
numb4 = mult_16(numb1, numb2)
print('Результат умножения чисел = ', end="")
print(*numb4, sep='')


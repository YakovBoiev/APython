"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections

numb_enterp = int(input('Введите количество предприятий '))
base_enterp = collections.defaultdict(list)
total_profit = 0
for _ in range(numb_enterp):
    name = input("Введите название предприятия ")
    for j in range(1, 5):
        base_enterp[name].append(float(input(f'Введите прибыль за {j} квартал ')))
    total_profit += sum(base_enterp[name])
midl_profit = total_profit / len(base_enterp)
print(f'Cредняя прибыль по всем предприятиям - {midl_profit}')
print("Предприятия с прибылью выше среднего: ")
for enterp in base_enterp:
    if sum(base_enterp[enterp]) >= midl_profit:
        print(enterp)
print("Предприятия с прибылью ниже среднего: ")
for enterp in base_enterp:
    if sum(base_enterp[enterp]) < midl_profit:
        print(enterp)


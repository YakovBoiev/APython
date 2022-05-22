"""""
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

https://drive.google.com/file/d/13RtWuDA6S2irtNrL4DO0X1vqJTTZ6KE6/view?usp=sharing

"""


n = int(input('Веедите натуральное число '))
leftsuq = 0
for i in range(1, n + 1):
    leftsuq += i
rightsuq = n * (n + 1) / 2
print(f'1+2+...+{n} = {leftsuq}')
print(f'{n}*({n}+1)/2 = {rightsuq}')
if leftsuq == rightsuq:
    print('Равенство доказано')
else:
    print('Равенство не доказано')
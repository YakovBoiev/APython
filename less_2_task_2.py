"""""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

https://drive.google.com/file/d/13RtWuDA6S2irtNrL4DO0X1vqJTTZ6KE6/view?usp=sharing
"""

numb = int(input('Введите натуральное число '))
evsumdig = 0
oddsumdig = 0
while True:
    dig = numb % 10
    if dig % 2 == 0:
        evsumdig += dig
    else:
        oddsumdig += dig
    if numb // 10 == 0:
        break
    else:
        numb = numb // 10
print(f'Сумма четных цифр - {evsumdig}')
print(f'Сумма нечетных цифр - {oddsumdig}')

"""""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

https://drive.google.com/file/d/13RtWuDA6S2irtNrL4DO0X1vqJTTZ6KE6/view?usp=sharing
"""

def summ_digit(numb):
    if numb // 10 == 0:
        return numb
    return numb % 10 + summ_digit(numb // 10)


maxsdigit = 0
nmaxdigit = 0
while True:
    numb = int(input('Введите натуральное число '))
    if numb <= 0:
        break
    else:
        sdigit = summ_digit(numb)
        if sdigit > maxsdigit:
            nmaxdigit = numb
            maxsdigit = sdigit
print(f'Число с максимальной суммой цифр  - {nmaxdigit}, сумма цифр  - {maxsdigit}')

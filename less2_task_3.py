"""""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.

https://drive.google.com/file/d/13RtWuDA6S2irtNrL4DO0X1vqJTTZ6KE6/view?usp=sharing
"""

def bw_number(numb):
    if numb // 10 == 0:
        return str(numb)
    return str(numb % 10) + str(bw_number(numb // 10))


numb = int(input('Введите число '))
bwnumb = bw_number(numb)
print(f'Обратное число {bwnumb}')

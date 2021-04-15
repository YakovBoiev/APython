""""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

https://drive.google.com/file/d/1pFXRM_lzv1wZ8hM0hx0sCNVnDCsogzZa/view?usp=sharing
"""
print('Введите три разных числа')
print('Введите первое число')
a = float(input())
print('Введите второе число')
b = float(input())
print('Введите третье  число')
c = float(input())
if a > b:
    if a < c:
        midl = a
    elif b > c:
        midl = b
    else:
        midl = c
else:
    if b < c:
        midl = b
    elif a > c:
        midl = a
    else:
        midl = c
print(f'Число {midl} является средним')

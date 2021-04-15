"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

https://drive.google.com/file/d/1pFXRM_lzv1wZ8hM0hx0sCNVnDCsogzZa/view?usp=sharing

"""
print('Введите трехзначное число')
a = int(input())
a = abs(a)
h = a // 100
t = a % 100 // 10
u = a % 10
s = h + t + u
m = h * t * u
print(f'Сумма цифр числа = {s}')
print(f'Произведение цифр числа = {m}')

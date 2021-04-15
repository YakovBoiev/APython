"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.

https://drive.google.com/file/d/1pFXRM_lzv1wZ8hM0hx0sCNVnDCsogzZa/view?usp=sharing
"""
print('Введите год')
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Год високосный')
        else:
            print('Год невисокосный')
    else:
        print('Год високосный')
else:
    print('Год невисокосный')

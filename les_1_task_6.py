"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква
https://drive.google.com/file/d/1pFXRM_lzv1wZ8hM0hx0sCNVnDCsogzZa/view?usp=sharing
"""

print('Введите номер буквы в алфавите')
num = int(input())
if num < 1 or num > 26:
    print('Буквы с данным номером в алфавите нет')
else:
    shift = ord('a') - 1
    let = chr(num + shift)
    print(f'Под номером {num} в алфавите буква - {let}')

""""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
https://drive.google.com/file/d/1pFXRM_lzv1wZ8hM0hx0sCNVnDCsogzZa/view?usp=sharing
"""

print('Введите букву № 1')
let1 = input()
print('Введите букву № 2')
let2 = input()
shift = ord('a') - 1
pos1 = ord(let1) - shift
pos2 = ord(let2) - shift
dist = abs(pos1 - pos2) - 1
if dist < 0:
    dist = 0
print(shift)
print(f'Номер места буквы  {let1}  в алфавите -  {pos1}')
print(f'Номер места буквы  {let2}  в алфавите -  {pos2}')
print(f'Между буквами {let1} и {let2} находятся {dist} букв')

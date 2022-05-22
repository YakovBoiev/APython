"""""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

https://drive.google.com/file/d/13RtWuDA6S2irtNrL4DO0X1vqJTTZ6KE6/view?usp=sharing
"""

start = 32
stop = 127
while start <= stop:
    for i in range(start, start + 10):
        if i > stop:
            break
        else:
            print(f'{i} - {chr(i)} ', end="")
    print()
    start += 10

def count_substr(s):
    substr_set = set()
    for j in range(len(s)):
        for i in range(j + 1, len(s) + 1):
            substr_set.add(hash(s[j:i]))
    return len(substr_set) - 1              # убираем из подсчета строку целиком

string = input("Введите строку ")
print(f'В строке {string} - {count_substr(string)} подстрок')


"""
Остались вопросы:
Я правильно понимаю что set внутри устроены как хэш таблицы?
Зачем тогда  в set добавлять hash а не сразу срезы? 
"""


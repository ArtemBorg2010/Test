import random

a = input()  # вводим слова
a = a.replace('+', ' ')  # убираем знаки
a = a.replace('=', ' ')  # убираем знаки
o = set(a)
a = a.split()  # а делим на слова
b = list(range(0, 10))  # список с цифрами от 0 до 9
c = [1000000000000000, 1, 0]  # список в котором будут уже числа вместо слов
s = {}  # словарь
x = 1
m = 0
if len(o) > 10:
    print('impossible')
else:
    popitka = 10 - (len(o) - 1)
    for v in range(10, popitka - 1, -1):
        x = x * v
    while int(c[0]) + int(c[1]) != int(c[2]):
        c = []
        for i in range(0, len(a)):  # перебираем а
            n = ''  # строка(слово из чисел)
            for f in range(0, len(a[i])):  # перебираем слово по буквам
                if a[i][f] not in s:  # если такой буквы не было в словаре
                    s[a[i][f]] = b.pop(
                        random.randrange(0, len(b)))  # добавляем в словарь буква - индекс, цифра - элемент
                n = n + str(s[a[i][f]])  # складываем цифры в 1 слово из цифр
            c.append(n)  # добавляем слово в список
        s = {}
        b = list(range(0, 10))
        m = m + 1
        if m >= x:
            print('impossible')
            break
    if m < x:
        print(str(c[0]) + '+' + str(c[1]) + '=' + str(c[2]))  # выводим его включая знаки

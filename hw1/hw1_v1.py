# Task 1

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if len(phrase_1) > len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
elif len(phrase_2) > len(phrase_1):
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы равной длины")

# Task 2

year = 2100

if year % 4 == 0:
    if ((year % 100) == 0) and ((year % 400) == 0):
        print("Високосный год")
    elif year % 100 == 0:
        print("Обычный год")
    else:
        print("Високосный год")
else:
    print("Обычный год")


# Task 3

print("Введите день и месяц своего рождения.")

day_of_birth = int(input("Введите день: "))
month_of_birth = input("Введите месяц: ")

if month_of_birth == "Январь":
    if day_of_birth < 20:
        print("Ваш знак зодиака: Козерог")
    else:
        print("Ваш знак зодиака: Водолей")
elif month_of_birth == "Февраль":
    if day_of_birth < 19:
        print("Ваш знак зодиака: Водолей")
    else:
        print("Ваш знак зодиака: Рыбы")
elif month_of_birth == "Март":
    if day_of_birth < 21:
        print("Ваш знак зодиака: Рыбы")
    else:
        print("Ваш знак зодиака: Овен")
elif month_of_birth == "Апрель":
    if day_of_birth < 20:
        print("Ваш знак зодиака: Овен")
    else:
        print("Ваш знак зодиака: Телец")
elif month_of_birth == "Май":
    if day_of_birth < 21:
        print("Ваш знак зодиака: Телец")
    else:
        print("Ваш знак зодиака: Близнецы")
elif month_of_birth == "Июнь":
    if day_of_birth < 21:
        print("Ваш знак зодиака: Близнецы")
    else:
        print("Ваш знак зодиака: Рак")
elif month_of_birth == "Июль":
    if day_of_birth < 23:
        print("Ваш знак зодиака: Рак")
    else:
        print("Ваш знак зодиака: Лев")
elif month_of_birth == "Август":
    if day_of_birth < 23:
        print("Ваш знак зодиака: Лев")
    else:
        print("Ваш знак зодиака: Дева")
elif month_of_birth == "Сентябрь":
    if day_of_birth < 23:
        print("Ваш знак зодиака: Дева")
    else:
        print("Ваш знак зодиака: Весы")
elif month_of_birth == "Октябрь":
    if day_of_birth < 23:
        print("Ваш знак зодиака: Весы")
    else:
        print("Ваш знак зодиака: Скорпион")
elif month_of_birth == "Ноябрь":
    if day_of_birth < 22:
        print("Ваш знак зодиака: Скорпион")
    else:
        print("Ваш знак зодиака: Стрелец")
elif month_of_birth == "Декабрь":
    if day_of_birth < 22:
        print("Ваш знак зодиака: Стрелец")
    else:
        print("Ваш знак зодиака: Козерог")
else:
    print("Уточните ввод.")

# Task 4

width = 15
length = 55
height = 15

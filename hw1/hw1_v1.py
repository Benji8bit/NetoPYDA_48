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

import sys

print("Введите день и месяц своего рождения.")

try:
    day_of_birth = int(input("Введите день: "))
except ValueError:
    print("Эх, нужно было вводить число...")
    sys.exit()
month_of_birth = input("Введите месяц: ")

if month_of_birth.capitalize() == "Январь":
    if 0 < day_of_birth < 20:
        print("Ваш знак зодиака: Козерог")
    elif 19 < day_of_birth < 32:
        print("Ваш знак зодиака: Водолей")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Февраль":
    if 0 < day_of_birth < 19:
        print("Ваш знак зодиака: Водолей")
    elif 18 < day_of_birth < 30:
        print("Ваш знак зодиака: Рыбы")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Март":
    if 0 < day_of_birth < 21:
        print("Ваш знак зодиака: Рыбы")
    elif 20 < day_of_birth < 32:
        print("Ваш знак зодиака: Овен")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Апрель":
    if 0 < day_of_birth < 20:
        print("Ваш знак зодиака: Овен")
    elif 19 < day_of_birth < 31:
        print("Ваш знак зодиака: Телец")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Май":
    if 0 < day_of_birth < 21:
        print("Ваш знак зодиака: Телец")
    elif 20 < day_of_birth < 32:
        print("Ваш знак зодиака: Близнецы")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Июнь":
    if 0 < day_of_birth < 21:
        print("Ваш знак зодиака: Близнецы")
    elif 20 < day_of_birth < 31:
        print("Ваш знак зодиака: Рак")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Июль":
    if 0 < day_of_birth < 23:
        print("Ваш знак зодиака: Рак")
    elif 22 < day_of_birth < 32:
        print("Ваш знак зодиака: Лев")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Август":
    if 0 < day_of_birth < 23:
        print("Ваш знак зодиака: Лев")
    elif 22 < day_of_birth < 32:
        print("Ваш знак зодиака: Дева")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Сентябрь":
    if 0 < day_of_birth < 23:
        print("Ваш знак зодиака: Дева")
    elif 22 < day_of_birth < 31:
        print("Ваш знак зодиака: Весы")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Октябрь":
    if 0 < day_of_birth < 23:
        print("Ваш знак зодиака: Весы")
    elif 22 < day_of_birth < 32:
        print("Ваш знак зодиака: Скорпион")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Ноябрь":
    if 0 < day_of_birth < 22:
        print("Ваш знак зодиака: Скорпион")
    elif 21 < day_of_birth < 31:
        print("Ваш знак зодиака: Стрелец")
    else:
        print("Уточните ввод дня.")
elif month_of_birth.capitalize() == "Декабрь":
    if 0 < day_of_birth < 22:
        print("Ваш знак зодиака: Стрелец")
    elif 21 < day_of_birth < 32:
        print("Ваш знак зодиака: Козерог")
    else:
        print("Уточните ввод дня.")
else:
    print("Уточните ввод месяца.")


# Task 4

width = 45
length = 205
height = 45

if width <= 15 and length <= 15 and height <= 15:
    print("Коробка №1")
elif width > 200 or length > 200 or height > 200:
    print("Упаковка для лыж")
elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
    print("Коробка №2")
else:
    print("Коробка №3")

# Task 5

number = 123456

if (number // 100000 + number % 100000 // 10000 + number % 10000 // 1000) == (
        number % 1000 // 100 + number % 100 // 10 + number % 10):
    print("Счастливый билет")
else:
    print("Несчастливый билет")

# Task 6

import math

figure_type = input("Введите тип геометрической фигуры: ")

if figure_type.capitalize() == "Круг":
    circle_radius = int(input("Введите длину радиуса круга: "))
    circle_square = math.pi * circle_radius ** 2
    print("Площадь круга: " + str(circle_square))

elif figure_type.capitalize() == "Треугольник":
    triangle_side_A = int(input("Введите длину стороны А: "))
    triangle_side_B = int(input("Введите длину стороны B: "))
    triangle_side_C = int(input("Введите длину стороны C: "))
    half_perimeter = (triangle_side_A + triangle_side_B + triangle_side_C) / 2
    triangle_square = math.sqrt(
        half_perimeter * (half_perimeter - triangle_side_A) * (half_perimeter - triangle_side_B) * (
                half_perimeter - triangle_side_C))
    print("Площадь треугольника: " + str(triangle_square))

elif figure_type.capitalize() == "Прямоугольник":
    rectangle_side_A = int(input("Введите длину стороны А: "))
    rectangle_side_B = int(input("Введите длину стороны B: "))
    rectangle_square = rectangle_side_A * rectangle_side_B
    print("Площадь прямоугольника: " + str(rectangle_square))

else:
    print("Какой блин гексаоктаэдр? Введите круг, треугольник или прямоугольник.")

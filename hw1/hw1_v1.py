# Task 1

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'

if (len(phrase_1) > len(phrase_2)):
    print("Фраза 1 длиннее фразы 2")
elif (len(phrase_2) > len(phrase_1)):
    print("Фраза 2 длиннее фразы 1")
else:
    print("Фразы равной длины")

# Task 2

year = 2020

if ((year%4)==0) and ((year%100)==0) and ((year%400)==0):
    print("Високосный год")
else:
    print("Обычный год")
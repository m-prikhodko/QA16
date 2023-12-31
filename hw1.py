# 1)Найти значения выражений:
print("Задание 1")
print("Значения выражений:")
# 17/2*3+2
task1 = 17 / 2 * 3 + 2
print("17/2*3+2 =", task1)
# 2+17/2*3
task2 = 2 + 17 / 2 * 3
print("2+17/2*3 =", task2)
# 19%4+15/2*3
task3 = 19 % 4 + 15 / 2 * 3
print("19%4+15/2*3 =", task3)
# 15+6-10*4
task4 = 15 + 6 - 10 * 4
print("15+6-10*4 =", task4)
# 17/2%2*3**3
task5 = 17 / 2 % 2 * 3 ** 3
print("17/2%2*3**3 =", task5)
print("______________")

# 2)Расставить скобки так, чтобы получился следующий результат:
print("Задание 2")
print("Получение нужного результата:")
# 42.5
task6 = 17 / 2 * (3 + 2)
print(task6, "= 17/2*(3+2)")
# 28.5
task7 = (2 + 17) / 2 * 3
print(task7, "= (2+17)/2*3")
# 0.0
task8 = 19 % (4 + 15) / 2 * 3
print(task8, "= 19%(4+15)/2*3")
# 44
task9 = ((15 + 6) - 10) * 4
print(task9, "= ((15+6)-10)*4")
# 8.5
task10 = (17 / 2) % (2 * 3 ** 3)
print(task10, "= (17/2)%(2*3**3)")
print("______________")

# 3) Анна пошла в магазин, у неё было 11 рублей. Хлеб стоит 1 рубль 50 копеек.
# анна купила 3 буханки хлеба. Сколько рублей у неё осталось?
print("Задание 3")
ann_money = 11
bread_cost = 1.50
bread_quantity = 3
print("У Анны осталось", ann_money - bread_quantity * bread_cost, "рублей.")
print("______________")

# 4) У Анны 2 яблока, у Пола 5 яблок. Выведите на экран сколько яблок у Пола и сколько яблок у Анны одной командой print(), использовать переменные.
print("Задание 4")
ann_apples = 2
paul_apples = 5
print("У Анны и Пола", ann_apples + paul_apples, "яблок.")
print("______________")

# 5) Напишите программу которая переводит число суток в часы, минуты и секунды. Задачу решить в 2 строчки.
# Формат вывода по образцу.
# days = 5
# Sample Output:
# 5 суток = 120 часов = 7200 минут = 432000 секунд
print("Задание 5")
days_1 = 5
print(days_1, "суток =", days_1 * 24, "часов =", days_1 * 1440, "минут =", days_1 * 86400, "секунд")
print("______________")

# 6) Напишите программу, которая вычисляет сколько полных недель прошло за период, если прошло 182 дня.
print("Задание 6")
days_2 = 182
week = 7
print("За", days_2, "прошло", days_2 // week, "полных недель")
print("______________")


# Дополнительные задачи:
#
# 7) Дан прямоугольник со сторонами a см и b см, сколько квадратов со стороной 30 см можно отрезать от него.
# a и b задаются в одной строке с клавиатуры.
# side_1 = 150  side_2 = 65
# Sample Output :
# Можно отрезать 10 квадратов.
print("Задание 7")
a, b = int(input("Введите длину (a) прямоугольника в см: ")), int(input("Введите ширину (b) прямоугольника в см: "))
sq_side = 30
print("Можно отрезать", (a // sq_side) * (b // sq_side), "квадратов.")
print("______________")

# 8) Дано число секунд. Вычислите сколько это часов, минут и секунд.
# seconds = 4000
# Sample Output :
# 1 час
# 6 минут
# 40 секунд
print("Задание 8")
seconds = 4000
hours = seconds // 3600
minutes = (seconds - (hours * 3600)) // 60
seconds_1 = seconds - ((hours * 3600) + (minutes * 60))
print(hours, "час")
print(minutes, "минут")
print(seconds_1, "секунд")
print("______________")

# 9) Нужно заплатить N рублей. Есть купюры 100, 50, 10, 1 руб.
# Сколько купюр каждого достоинства нужно отдать покупателю, если он будет платить с самых крупных.
# cash = 361
# Sample Output :
# 3 купюры по 100 рублей
# 1 купюры по 50 рублей
# 1 купюры по 10 рублей
# 1 купюры по 1 рублей
print("Задание 9")
cash = 361
banknote100 = cash // 100
banknote50 = (cash - (banknote100 * 100)) // 50
banknote10 = (cash - (banknote100 * 100 + banknote50 * 50)) // 10
banknote1 = (cash - (banknote100 * 100 + banknote50 * 50 + banknote10 * 10)) // 1
print(banknote100, "купюры по 100 рублей")
print(banknote50, "купюры по 50 рублей")
print(banknote10, "купюры по 10 рублей")
print(banknote1, "купюры по 1 рублей")
print("______________")

# 10) Улитка ползет по вертикальному шесту высотой h метров, поднимаясь за день на x метров, а за ночь спускаясь на y метров.
# На какой день улитка доползет до вершины шеста?
print("Задание 10")
h = 10
x = 5
y = 2
finish_per_day = x - y
finish_final = h // finish_per_day
print("Улитка доползет до вершины шеста на", finish_final, "день.")
print("______________")

# 11) Длина Минской кольцевой автомобильной дороги —56 километров.
# Байкер  стартует с нулевого километра МКАД и едет со скоростью V километров в час. На какой отметке он остановится через T часов M минут?
print("Задание 11")
road_length = 56
v = 90
t = 3
m = 40
print("Байкер остановится на отметке", (v * t + (v / 60 * m)) % road_length, "км через", t, "часов", m, "минут.")
print("______________")
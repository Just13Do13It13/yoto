# x = int(input("Введи число: "))
# if x > 0:
#     print("Число положительное: ")
# elif x < 0:
#     print("Число отрицательное")
# else:
#     print("Число равно нулю")


# z = int(input("Введи целое число: "))
# if z >= 0 and z <= 10:
#     print("Число в диапазоне")
# else:
#     print("Число вне диапазона")

# z1 = int(input("Число a: "))
# z2 = int(input("Число b: "))
# if z1 < z2:
#     z1, z2 = z2, z1
#     print(z1, z2)


# z3 = int(input("Число a: "))
# z4 = int(input("Число b: "))
# min_ab = min(z3, z4)
# print(min_ab)

# marks = [3, 4, 5, 2, 5, 4]
# if 2 in marks:
#     print("Есть неудовлетворительная оценка")
# else:
#     print("Все оценки положительные")


# ffs = int(input("Число a: "))
# if ffs % 3 == 0 and ffs % 5 == 0:
#     print("Число делится на 3 и 5")
# elif ffs % 3 == 0:
#     print("Число делится только на 3")
# elif ffs % 5 == 0:
#     print("Число делится только на 5")
# else:
#     print("Число не делится на 3 и 5")


# ffs = input("Пароль, гнида: ")
# if ffs == "admin123":
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# amount = int(input("Сумма покупки: "))
#
# if amount >= 5000:
#     discount = amount * 0.10
#     print(f"Ваша скидка равна: {discount} руб.")
#     print(f"Итоговая сумма для оплаты равна: {amount - discount} руб.")
# elif amount >= 1000:
#     discount = amount * 0.05
#     print(f"Ваша скидка равна: {discount} руб.")
#     print(f"Итоговая сумма для оплаты равна: {amount - discount} руб.")
# else:
#     print("Нет скидки")

# god = int(input("Введи год: "))
# if god % 4 == 0 and not god % 100 == 0 and not god % 400 == 0:
#     print("Год високосный")
# else:
#     print("Год не високосный")
# god = int(input("Введи 1-5: "))
# if god == 5:
#     print("Атлишна")
# elif god == 4:
#     print("Норм")
# elif god == 3:
#     print("Так се")
# elif god == 2 or god == 1:
#     print("Стрем")
# else:
#     print("Не то ввел")
# god = int(input("Введи текущее время 0-24: "))
# if 6 <= god <= 11:
#     print("Утро")
# elif 12 <= god <= 17:
#     print("День")
# elif 18 <= god <= 21:
#     print("Вечер")
# elif god >= 22 or god <= 5:
#     print("Ночь")
# else:
#     print("Чет не то")
# god = int(input("Введи температуру: "))
# if god < -10:
#     print("Морозит")
# elif -10 <= god <= 0:
#     print("Прохладно")
# elif 1 <= god <= 10:
#     print("Norm")
# elif 11 <= god <= 25:
#     print("Тепло")
# elif god > 25:
#     print("Жара")
# else:
#     print("Чет не то")
# god = int(input("Введи год: "))
# if god % 4 == 0 and not god % 100 == 0 and not god % 400 == 0:
#      print("Год високосный")
# else:
#    print("Год не високосный")
# a = int(input("Введи число первое: "))
# b = int(input("Введи число второе: "))
# c = input("Че хочешь сделать?: ")
# if c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "*":
#     print(a * b)
# elif c == "/":
#     print(a / b)
# else:
#     print("Ввел не то")
# number = int(input("Введи число: "))
#
# print("Чётное" if number % 2 == 0 else "Нечётное")
# number1 = int(input("Введи число: "))
# number2 = int(input("Введи число: "))
# print(max(number1, number2))
# number = int(input("Введи число: "))
# if 0 > number:
#     print(number, "отрицательное")
# elif 0 < number:
#     print(number, "Положительное")
# else:
#     print(number, "Ноль")
# Vxod = int(input("Введи Свой возраст: "))
# if 18 <= Vxod <= 55:
#     print("Молодежь")
# elif 56 <= Vxod <= 100:
#     print("Пенсия)")
# elif Vxod < 18:
#     print("Запрещено")
# else:
#     print("Тебе не может быть так много лет ОБМАНЩИК)")
# Sum = int(input("Введи сумму покупки: "))
# if Sum > 5000:
#     print(f"У вас прошла скидка 10% = {Sum * 0.1}РУБ. и итоговая сумма к оплате будет = {Sum-(Sum * 0.1)} РУБ.")
# elif Sum <= 5000:
#     print(f"Скидки нет, сумма к оплате {Sum}")
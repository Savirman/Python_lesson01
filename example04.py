# Программе нахождения наибольщей цифры в числе

# Пользователь вводит целое число произвольной длины
while True:
    number = int(input("Введите целое положительное число: "))
# Проверяем введенное число. Если оно отрицательное, то выдаем сообщение об этом и просим ввести положительное число
    if number < 0:
        print("Вы ввели отрицательное число. Введите положительное число")
    else:
        number = str(number)
        break

# Запускаем цикл с поиском цифр в числе от 9 до 0
counter = 9
while counter >= 0:
    biggest_digit = '9'
    biggest_digit = str(counter)
    if biggest_digit in number:
        print("Самая большая цифра в числе: {}".format(biggest_digit))
        break
    counter = counter - 1

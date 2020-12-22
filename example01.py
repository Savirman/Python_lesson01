# Создание переменных a, b, c

a = 14
b = 20.4
c = "This is a string"

# Вывод переменных на экран

print(a)
print(b)
print(c)

# Запрос у пользователя чисел и строк

number_int = int(input("Введите целое число: "))
number_float = float(input("Введите число с плавающей точкой: "))

username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

print("Введенные числа: " '%d, %f' % (number_int, number_float))
print("Имя пользователя: " '%s' % (username))
print("Пароль: " '%s' % (password))

# Программы суммирования чисел n, nn, nnn

# Ввод пользователем числа с соханением в виде строки
n = input("Введите число n: ")

# Нахождение числа nn путем склеивания двух строк n и последующем преобразование получившейся строки в целое число
nn = int(n + n)

# Нахождение числа nnn путем склеивания трех строк n и последующем преобразование получившейся строки в целое число
nnn = int(n + n + n)

# Преобразование строки n в целое число
n = int(n)

# Нахождение суммы чисел
sum = n + nn + nnn

# Вывод суммы чисел на экран
print(sum)
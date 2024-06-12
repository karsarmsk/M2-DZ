# Задание "Слишком древний шифр":
# 9 - число из первой вставки
# 1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
# 1+2 =3
# 9 кратно сумме чисел
def generate_password(n):  # функция пароль где n число из первой вставки
    password = ''          # создаем пустую строку пароль.
    for i in range(1,21):  # цикл от 0 до 20 для первого числа в паре
        for j in range(i + 1, 21):  # цикл от 1 до 20 для второго числа в паре
            if n % (i +j) == 0:  # если число делится без остатка на суммму чисел из пары
                password += str(i) + str(j)  # в строку рароль вписываем пару
    return password  # возвращаем пароль

attempt = 0
while attempt <= 20:  # цикл на 20 попыток получения пароля
    n = int(input('Ввод числа: '))
    if n >= 3 and n <= 20:  # проверка на правильность ввода числа
        print(f'{n} - {generate_password(n)}')  # Вызов функции и Вывод пароля
        attempt += attempt
    else:
        attempt = 0
        print('Число не то')

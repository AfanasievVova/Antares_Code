#Три последовательных числа

first_number = int(input(""))


second_number = first_number + 1
third_number = first_number + 2

print(first_number)
print(second_number)
print(third_number)

#Сумма трёх чисел

first_number = int(input(""))
second_number = int(input(""))
third_number = int(input(""))

sum_of_numbers = first_number + second_number + third_number
print(sum_of_numbers)

# объём куба и площадь
# Запрос длины ребра куба у пользователя
edge_length = float(input("Объем ="))

# Вычисление объема куба
volume = edge_length ** 3

# Вычисление площади полной поверхности куба
surface_area = 6 * (edge_length ** 2)

# Вывод результатов на экран без нулей в конце
print("", "{:.2f}".format(volume).rstrip('0').rstrip('.'))
print("Площадь полной поверхности =", "{:.2f}".format(surface_area).rstrip('0').rstrip('.'))

#Значение функции F(x)

def compute_function(a, b):
    # Вычисляем (a + b)^3
    sum_ab = a + b
    sum_ab_cubed = sum_ab * sum_ab * sum_ab

    # Вычисляем значение функции
    result = 3 * sum_ab_cubed + 275 * b * b - 127 * a - 41

    return result


# Чтение входных данных
a = int(input())
b = int(input())

# Вычисление и вывод результата
print(compute_function(a, b))

#Следующее и предыдущее

# Считываем целое число
number = int(input())

# Вычисляем следующее и предыдущее число
next_number = number + 1
previous_number = number - 1

# Форматируем и выводим результат
print(f"Следующее за числом {number} число: {next_number}")
print(f"Для числа {number} предыдущее число: {previous_number}")

#Стоимость покупки 🛒



# Читаем стоимости компонентов
monitor_cost = int(input())
cpu_cost = int(input())
keyboard_cost = int(input())
mouse_cost = int(input())

# Рассчитываем стоимость одного компьютера
computer_cost = monitor_cost + cpu_cost + keyboard_cost + mouse_cost

# Рассчитываем стоимость трех компьютеров
total_cost = 3 * computer_cost

# Выводим результат
print(total_cost)

#Арифметические операции


a = int(input())
b = int(input())

# Вычисляем сумму, разность и произведение
sum_result = a + b
difference_result = a - b
product_result = a * b

# Выводим результаты в указанном формате
print(f"{a} + {b} = {sum_result}")
print(f"{a} - {b} = {difference_result}")
print(f"{a} * {b} = {product_result}")

#Арифметическая прогрессия

# Считываем входные данные
a1 = int(input())
d = int(input())
n = int(input())

# Вычисляем n-ый член арифметической прогрессии
an = a1 + d * (n - 1)

# Выводим результат
print(an)

#Геометрическая прогрессия
# Чтение входных данных
b1 = int(input())
q = int(input())
n = int(input())

# Вычисление n-го члена геометрической прогрессии
bn = b1 * (q ** (n - 1))

# Вывод результата
print(bn)

#Расстояние в метрах
#Напишите программу, которая находит полное число метров по заданному числу сантиметров.

centimeters = int(input())

meters = centimeters // 100
print(meters)

#Мандарини
# Чтение входных данных
n = int(input())  # Количество школьников
k = int(input())  # Количество мандаринов

# Вычисление количества мандаринов на одного школьника и остатка
if n > 0:  # Проверяем, что количество школьников больше 0
    mandarins_per_student = k // n
    remaining_mandarins = k % n
else:
    mandarins_per_student = 0
    remaining_mandarins = k

# Вывод результатов
print(mandarins_per_student)
print(remaining_mandarins)

#Сама неотвратимость
import math

# Чтение входного значения
n = int(input().strip())

# Вычисление количества выживших
survivors = math.ceil(n / 2)

# Вывод результата
print(survivors)

#Пересчёт временного интервала
# Чтение входного значения
total_minutes = int(input().strip())

# Определение количества полных часов и оставшихся минут
hours = total_minutes // 60
minutes = total_minutes % 60

# Формирование и вывод результата
print(f"{total_minutes} мин - это {hours} час {minutes} минут.")

#номер в купе
# Чтение номера места
place_number = int(input().strip())

# Определение номера купе
compartment_number = (place_number - 1) // 4 + 1

# Вывод результата
print(compartment_number)

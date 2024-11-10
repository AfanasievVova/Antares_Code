def hello():
    print("Hello, world!")


hello()


# ==================================== # вивести привет мир

def add(number, number1):
    print(number + number1)


add(2, 5)


# ==================================== додать цифру 2 + 5
def add_number(number3, number4):
    return number3 + number4


result = add_number(2, 8)
print(result)
twice = result * 2
print(twice)


# ==================================== с начало ми додаем а потом умножаем

def greeter(name):
    return f"Hi, {name}!"


print(greeter("Bob"))


# ==================================== вивести имя

def math(number):
    if number == 785:
        return "No"
    elif number >= 670:
        return "Okay"
    else:
        return "N"


print(math(800))


# ==================================== понять какое число истина что больше что меньше

def greeter(name, part_of_the_day):
    return f"Good {part_of_the_day}, {name}!"


print(greeter("Max", "night"))


# ==================================== виводит просто имя и ночь

def add_numbers(number6, number5):
    return number6 + number5


print(add_numbers(3, 6))


# ==================================== снова добовляем цифру

def name(age):
    for i in range(1, 101):
        print(i)
    if age == 59:
        return "num 1"
    elif age >= 30:
        return "num 2"
    else:
        return "Dolboeb"


print(name(40))


# ==================================== проверяем число больше менше

def double(num):
    result = num * 2
    return result


# Тестируем функцию
print(double(5))  # Ожидается вывод: 10


# ==================================== умножаем

def add_interest(balance, interest_rate):
    new_balance = balance + (balance * interest_rate / 100)
    return new_balance


initial_balance = 1000
new_balance = add_interest(initial_balance, 5)
result_balance = add_interest(new_balance, 5)


# ==================================== проверяем сколько мы получим процентов а 1 год и за 2

def temperature(value):
    if value > 19:
        return "Cold"
    elif value > 34:
        return "Warm"
    elif value < 9:
        return "Hot"


print(temperature(20))


# ==================================== проверяем истину погоди

def double_numbers(numbers):
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    return doubled


print(double_numbers([1, 2, 3, 4, 5]))


# ==================================== умножаем списки 1 * 2 = 2  2 * 2 = 4 и так дале пока не выйдет 10

def double_until_greater_than_100(num):
    result = []
    while num <= 100:
        result.append(num)
        num *= 2
    return result


print(double_until_greater_than_100(10))


# ==================================== умножаем 10 * 2 = 20 потом 20 * 2 = 40 потом так дале но у нас стоит макс до 100 то выйдет до 80 как 40 * 2 = 80

def add_fruit(fruit_list, fruit):
    if fruit not in fruit_list:
        fruit_list.append(fruit)
    return fruit_list


fruits = ["apple", "banana", "cherry"]
print(add_fruit(fruits, "orange"))


# ==================================== тут ми добовляем в список еше текст

def get_lists_sum(ls1, ls2):
    return sum(ls1) + sum(ls2)


print(get_lists_sum([1, 2], [3, 4]))


# ==================================== добовляем числа в списке как роботает у нас есть список ls1, ls2 с начало у нас добовляеться 1 + 3 = 4 потмо 2 + 4 = 6 4 + 6 = 10 все

def combine_lists(ls1, ls2):
    result_list = []
    for i in range(len(ls1)):
        result_list.append(ls1[i] + ls2[i])
    return result_list


print(combine_lists([1, 5, 6], [6, 7, 2]))


# ==================================== если нам нужно додать число но чтоб оно показало его в списке то мы пишем такой код вот так будет он виглдеит [7] все

def sum_two_lists(list1, list2):
    result_list = []
    for i in range(len(list1)):
        result_list.append(list1[i] + list2[i])
    return result_list


print(sum_two_lists([1, 2], [3, 4]))


# ==================================== мы снова додаем цифри но виводит виде списка как оно робоатет у нас есть [1, 2] [3, 4]
# с начало доадеться 1 + 3 = 4 потмо 2 + 4 = 6 и оно виводит вот так [4, 6]

# ================================= мы проверяем голосние букви есть ли в слове голосние букви
def remove_vowels(document):
    vowels = "aeiouyAEIOUY"
    result_string = ""

    for char in document:
        if char not in vowels:
            result_string += char

    return result_string


print(remove_vowels("captain"))


# ===================================== тут ми делаем стикери для робот точне детали

def make_stickers(details_count, robot_part):
    stickers = []

    for i in range(1, details_count + 1):
        stickers.append(f"{robot_part} detail #{i}")

    return stickers


print(make_stickers(3, "Body"))


# =================================================== тут у нас делатли создаються в 2 раза больше стало

def double_power(current_powers):
    result_list = []
    for i in range(len(current_powers)):
        result_list.append(current_powers[i] * 2)
    return result_list


print(double_power([100, 150, 200, 220]))


# ======================================== щас мы даем команди роботу

def get_location(coordinates, commands):
    x, y = coordinates
    for command in commands:
        if command == "forward":
            y += 1
        elif command == "back":
            y -= 1
        elif command == "right":
            x += 1
        elif command == "left":
            x -= 1
    return [x, y]


print(get_location([0, 0], ["forward", "right"]))


# ================================== тут ми учим роботов сортувать коробки

def is_sorted(box_numbers):
    return box_numbers == sorted(box_numbers)


print(is_sorted([1, 2, 3, 4, 5]))


def sorted_is(box_num):
    return box_num == sorted(box_num)


print(sorted_is([1, 2, 3, 4, 5]))


# ======================================== скоротить код на умножение списков

def double(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    return [number * 2 for number in numbers]


print(double())
# ==========================================

import math


def get_plan(current_production, months, percent):
    # Список для зберігання цілей на кожен місяць
    plan = []

    # Для кожного місяця
    for _ in range(months):
        # Округлене значення виробництва для поточного місяця
        plan.append(math.floor(current_production))
        # Оновлюємо виробництво на наступний місяць
        current_production += current_production * (percent / 100)

    return plan


print(get_plan(10, 4, 30))

# ==========================================================

import math


def get_plan(current_production, months, percent):
    plan = []
    for _ in range(months):
        # Обчислити нову кількість роботів
        current_production = math.floor(current_production * (1 + percent / 100))
        # Додати до списку
        plan.append(current_production)
    return plan


# Тести
print(get_plan(200, 3, 50))  # [300, 450, 675]
print(get_plan(10, 4, 30))  # [13, 16, 20, 26]
print(get_plan(1000, 6, 20))  # [1200, 1440, 1728, 2073, 2487, 2984]

# ===========================================  скорость роботов

import math


def get_speed_statistic(test_results):
    if not test_results:
        return [0, 0, 0]

    min_speed = min(test_results)
    max_speed = max(test_results)
    avg_speed = math.floor(sum(test_results) / len(test_results))

    return [min_speed, max_speed, avg_speed]


# Тести
print(get_speed_statistic([]))  # [0, 0, 0]
print(get_speed_statistic([10]))  # [10, 10, 10]
print(get_speed_statistic([8, 9, 3, 12]))  # [3, 12, 8]
print(get_speed_statistic([10, 10, 11, 9, 12, 8]))  # [8, 12, 10]


#============================================= виводить имя в тексте

def greet(name):
    # Выводим текст
    print(f"Привет, {name}!")

    # Возвращаем значение name
    return name


# Вызов функции и сохранение результата
result = greet("Анна")

# Вывод результата
print(f"Возвращенное значение: {result}")

# ============================================

def number(ok):
    okey = []
    for i in range(len(ok)):
        okey.append(ok[i] * 2)
    return okey


print(number([100, 150, 200, 220]))

# ======================================

def con(detali, comand):
    x, y = detali
    for command in comand:
        if command == "forward":
            y += 1
        if command == "back":
            y -= 1
        if command == "left":
            x += 1
        if command == "right":
            x -= 1

    return [x, y]


print(con([0, 0], ["right", "forward"]))

# =============================================

def i(lists1, lists2):
    results_lists = []
    for ino in range(len(lists1)):
        results_lists.append(lists1[ino] + lists2[ino])
    return results_lists


print(i([2, 46, 68], [30, 45, 657]))

# ==================================

def home(homes):
    result_list = []
    for hom in range(len(homes)):
        result_list.append(homes[hom] ** 2)
    return result_list


print(home([4]))

# =====================================

def math(programming):
    return f"Hello, {programming}"

print(math("Alex"))

# ==================================

def friend(x):
    for name_friends in x:
        if len(x) == 4:
            return x


print(friend(input()))

# ===========================

def friend(x):
    name_friends = ["Ryan", "Kieran", "Jason", "Yous"]
    result = []
    for name in name_friends:
        if len(name) == x:
            result.append(name)
    return result

print(friend(4))

# ================================

def number(num1, num2):
    result_list = []
    for i in range(len(num1)):
        result_list.append(num1[i] ** num2[i])
    return result_list


print(number([10, 4], [10, 6]))

# ===============================
def name_friends(x):
    for friends in x:
        if len(x) == 4:
            return x


print(name_friends(input()))

#= =================================

def boolean_to_string(b):
    return str(b)

# ==================================

def square_sum(numbers):
    result_sum = 0
    for num in numbers:
        result_sum += num ** 2
    return result_sum

print(square_sum([1, 2, 2]))  # Вывод: 9

# ==================================
def number(num):
    result_sum = 0
    for numbers in num:
        result_sum += numbers ** 2
    return result_sum

print(number([1, 2, 2]))

# ================================

def grow(arr):
    result_num = 1
    for num in arr:
        result_num *= num
    return result_num


print(grow([1, 2, 3, 4]))

#====================================
def maps(a):
    result_list = []
    for i in range(len(a)):
        result_list.append(a[i] * 2)
    return result_list


print(maps([1, 2, 3]))

# ========================================

def find_smallest_int(arr):
    return min(arr)

arr =  [34, -345, -1, 100]
print(find_smallest_int(arr))

# ===========================================

happy_friends = ["Egor", "Vova", "Kir"]

for friend in happy_friends:
    print(f'Hello my bro {friend}')

# =============================================

happy_stol = ['Vova', 'Nestor', 'Kir']
happy_stol.insert(0, 'bob')
happy_stol.insert(2, "Alex")
happy_stol.append("Egor")
for happy in happy_stol:
    print(f"guys big stol {happy}")

# ============================================== Calculator

def get_multiplication_result(a, b):
    return a * b

def get_division_result(a, b):
    return a / b

def get_addition_result(a, b):
    return a + b

def get_subtraction_result(a, b):
    return a - b

def get_squaring(a, b):
    return a ** b

def calculator(operator, a, b):
    if operator == "*":
        return get_multiplication_result(a, b)
    elif operator == "/":
        return get_division_result(a, b)
    elif operator == "+":
        return get_addition_result(a, b)
    elif operator == "-":
        return get_subtraction_result(a, b)
    elif operator == "**":
        return get_squaring(a, b)


operator = input()
a = float(input())
b = float(input())

result = calculator(operator, a, b)
print("Result", result)


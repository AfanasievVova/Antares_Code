num = 17
s = str(num)
print(s)

num = '17'
s = int(num)
print(s)


first_number = int(input(""))


second_number = first_number + 1
third_number = first_number + 2

print(first_number)
print(second_number)
print(third_number)


v = 25 ** 3
print(v)

s = 6 * 25 ** 2
print(s)

def get_volume_area():
    """ найти area and volume куба """
    x_25 = int(input())
    v = x_25 ** 3
    s = 6 * x_25 ** 2
    print(f"Объем = {v}")
    print(f"Площадь полной поверхности = {s}")

get_volume_area()

# Запрос длины ребра куба у пользователя

def get_function():
    function = 3 * ((a + b) ** 3) + (275 * b ** 2) - (127 * a) - 41
    return function
a = int(input())
b = int(input())

print(get_function())

def get_sum_number():
    get_num_1 = int(input())
    get_num_2 = int(input())
    get_num_3 = int(input())
    result = get_num_1 + get_num_2 + get_num_3
    return result


print(get_sum_number())

def number():
    a = int(input())
    a_1 = a
    a_2 = a + 1
    a_3 = a + 2

    print(a_1)
    print(a_2)
    print(a_3)

number()

def number():
    number_b = int(input())
    result_1 = number_b + 1
    result_2 = number_b - 1
    print(f"Следующее за числом {number_b} число: {result_1}")
    print(f"Для числа {number_b} предыдущее число: {result_2}")



number()

def buy():
    buy_1 = int(input())
    buy_2 = int(input())
    buy_3 = int(input())
    buy_4 = int(input())
    result_cost = buy_1 + buy_2 + buy_3 + buy_4
    return result_cost * 3


print(buy())

def number():
    a = int(input())
    b = int(input())
    result_1 = a + b
    result_2 = a - b
    result_3 = a * b
    print(f"{a} + {b} = {result_1}")
    print(f"{a} - {b} = {result_2}")
    print(f"{a} * {b} = {result_3}")


number()


x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')

num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')

a = int(input())

if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)

def intrigel():
    x = int(input())
    if (-3 <= x <= 7):
        return "Принадлежит"
    else:
        return "Не принадлежит"

print(intrigel())

def intrigel():
    x = int(input())
    if x <= -3 or x >= 7:
        return "Принадлежит"
    else:
        return "Не принадлежит"

print(intrigel())

def Triangle_inequality():
    a = int(input())
    b = int(input())
    c = int(input())

    if (a + b > c) and (a + c > b) and (b + c > a):
        return "YES"
    else:
        return "NO"

print(Triangle_inequality())

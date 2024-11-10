def add_binary(a,b):
    result = a + b
    return bin(result)[2:]


print(add_binary(1, 1))

def abs_func(num):
    return abs(num)


print(abs_func(-5))

def high_and_low(numbers):
    # Преобразуем строку в список целых чисел
    numbers = list(map(int, numbers.split()))
    # Находим максимум и минимум
    result = (max(numbers), min(numbers))
    # Возвращаем их в виде строки
    return f"{max(numbers)} {min(numbers)}"

# Тестируем с правильным входом
print(high_and_low("1 2 3 4 5"))  # Вывод: '5 1'


def get_sum(a,b):
    result = a + b
    return result

print(get_sum(-1, 0))

def get_sum(a,b):
    result = a + b
    return

print(get_sum(1, 0))

def maps(a):
    return [a[i] * 2 for i in range(len(a))]


print(maps([1, 2, 3]))

def invert(lst):
    return [-abs(lst[i]) for i in range(len(lst))]


print(invert([1, 2, 3, 4, 5]))

import math

def century(year):
    centurys = math.ceil(year / 100)
    return centurys


print(century(1705))

lists = [1, 2, 3]
result = sum(lists)
print(result)

def sum_array(a):
    result = sum(a)
    return result

print(sum_array([1, 5.2, 4, 0, -1]))

def sum_excluding_min_max(arr):
    if len(arr) <= 2:
        return 0  # Если элементов меньше или равно 2, то возвращаем 0
    return sum(arr) - max(arr) - min(arr)

print(sum_excluding_min_max([1, 2, 3, 234]))

def no_space(x):
    result = x.replace(" ", "")  # Заменяем все пробелы на пустую строку
    return result

print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B 8j8mBliB8gimjB8B8jlB"
"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))


import math

def grow(arr):
    result = math.prod(arr)
    return result


print(grow([1, 2, 3, 4]))

def reverse_seq(n):
    spam = list(range(1, n + 1))
    spam = spam[::-1]
    return spam

print(reverse_seq(5))

def lists(list):
    result = list.join(list)
    return result


print(lists("Strings"))

def min_max(lst):
    result = [min(lst), max(lst)]
    return result


print(min_max([1, 2, 3, 4, 5]))


names = ["Анна", "Максим", "Оля", "Ира"]  # пример списка
for name in names:
    if len(name) == 3:
        print(name)


def validate_pin(pin):
    if len(pin) == 4:
        return True


print(validate_pin("1234"))

def repeat_str(repeat, string):
    for i in range(repeat):
        print(string)


repeat_str(6, "I")

def goals(laLiga, copaDelRey, championsLeague):
    result = laLiga + copaDelRey + championsLeague
    return result



print(goals(5, 10, 2))

def find_smallest_int(arr):
    result = min(arr)
    result1 = max(arr)
    return result


print(find_smallest_int([34, 15, 88, 2]))
print(find_smallest_int([34, -345, -1, 100]))


def hula_hoop(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"


print(hula_hoop(9))

def check_for_factor(base, factor):
    if factor % base:
        return True
    else:
        return False

print(check_for_factor(10, 2))
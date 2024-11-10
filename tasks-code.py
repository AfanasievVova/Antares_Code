def add_interest(balance, interest_rate):
    new_balance = balance + (balance * interest_rate / 100)
    return new_balance


# Початковий баланс
initial_balance = 1000

# Розрахунок балансу після першого року з відсотковою ставкою 5%
new_balance = add_interest(initial_balance, 5)

# Розрахунок балансу після другого року з тим самим відсотком
result_balance = add_interest(new_balance, 5)

# Виведення результатів на екран
print(f"Баланс після першого року: {new_balance}")
print(f"Баланс після другого року: {result_balance}")


def add_fruit(fruit_list, fruit):
    if fruit not in fruit_list:
        fruit_list.append(fruit)
    return fruit_list

fruits = ["apple", "banana", "cherry"]
print(add_fruit(fruits, "orange"))


def double_until_greater_than_100(num):
    result = []
    while num <= 100:
        result.append(num)
        num *= 2
    return result


print(double_until_greater_than_100(10))


def categorize_temperature(temp):
    if temp > 30:
        return "Hot"
    elif 20 <= temp <= 30:
        return "Warm"
    elif 10 <= temp < 20:
        return "Cool"
    else:
        return "Cold"


print(categorize_temperature(15))


def double_numbers(numbers):
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    return doubled


print(double_numbers([1, 2, 3, 4, 5]))


def get_lists_sum(ls1, ls2):
    total_sum = sum(ls1) + sum(ls2)
    return total_sum


get_lists_sum([1, 2], [3, 4])


def number(numbers):
    var = []
    for num in numbers:
        var.append(num * 2)
    return var


print(number([1, 2, 3, 4, 5]))


def combine_lists(ls1, ls2):
    result_list = []
    for num in ls1, ls2:
        total_sum = sum(ls1) + sum(ls2)
    return total_sum


print(combine_lists([1, 2, 5], [3, 6, 1]))

def combine_lists(ls1, ls2):
    result_list = []
    for num in ls1, ls2:
        total_sum = sum(ls1) + sum(ls2)
    return total_sum


print(combine_lists([1], [6]))


def rating(ls3, ls4, ls5):
    total_sum = sum(ls3) * sum(ls4) + sum(ls5)
    return total_sum

# Пример использования:
print(rating([1, 2, 3], [4, 5, 6], [7, 8, 9]))  # Ожидаемый результат: 231


def sum_two_lists(list1, list2):
    result_list = []
    for lists in range(len(list1)):
        result_list.append(list1[lists] + list2[lists])
    return result_list

print(sum_two_lists([1, 2], [3, 4]))

def remove_vowels(document):
    vowels = "aeiouyAEIOUY"
    result_string = ""
    for char in document:
        if char not in vowels:
            result_string += char
    return result_string

print(remove_vowels("captain"))
print(remove_vowels("I like my boss"))
print(remove_vowels("350 euro"))
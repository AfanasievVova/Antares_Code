def name():
    number = 34
    if number < 300:
        print("Yes")
    else:
        print("No")


name()


def greeting(nam):
    print(f"Hello {nam}")


greeting("Alice")
greeting("Vova")


def add(number1, number2):
    print(number1 + number2)


add(2, 5)


def numbe(number3, number4):
    print(number3 - number4)


numbe(90, 23)


def add_numbers(numbers1, numbers2):
    return numbers1 + numbers2


result = add_numbers(90, 95)
print(result)
twice = result * 2
print(twice)


def movie_rating(age):
    if age < 15:
        return "PG"
    elif age <= 80:
        return "PG-13"
    else:
        return "N"


print(movie_rating(13))


def get_strings():
    greetings = "Hello, Mate academy!"
    return greetings


def greeter(names):
    return f"Hi, {names}!"


def greeters(names, part_of_the_day):
    return f"Good {part_of_the_day}, {names}!"


def double(num):
    return num * 2


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


def temperature(value):
    if value > 20:
        return "Cold"
    elif value < 50:
        return "Hot"
    else:
        return "Warm"


temperature(30)

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
#
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
for num in range(5, 16):
    print(num)

number = 0

for num in range(1, 16):
    number = number + num
print(number)

numbers = 0

for number in range(5, 16):
    numbers = numbers + number
print(numbers)


numberr = 0
for numbers in range(5, 16):
    numbers += numbers + numbers + numbers
    print(numbers)

trees = ["Redwood", "Birch", "Oak", "Pine", "Willow"]
for tree in trees:
    print(tree)

initial_distance = 5
increment = 2
total_weeks = 10

for month in range(5, 25, 2):
    initial_distance += increment
    increment += total_weeks
    print(month)

money = 100
book_price = 20
book = 0

while money >= book_price:
    money -= book_price
    book += 1
    print(f"Book Bought: {book}: money {money}")

countdown_start = 11
while countdown_start > -1:
    countdown_start += -1
    print(countdown_start)

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)

savings = 500
book_python_price = 100
book = 0
while savings >= book_python_price:
    savings -= book_python_price
    book += 1
    print(f"Book {book}: Money {savings}")

num = 0
for number in range(1, 11):
    num += number
    print(num)

for number in range(2, 22, 2):
    print(number)

lists = ["90", "80", "45", "45", "48"]
for item in lists:
    print(item)

# Факториал
n = 5

factorial = 1

for i in range(1, n + 1):
    factorial *= i
    print(factorial)

i = 1
while i <= 10:
    print(i)
    i += 1
# Четное нечетное
x = 1
while x <= 20:
    if x % 2 != 0:
        print(x)
        x += 1
i = 0
while i < 5:
    print(i)
    i += 1


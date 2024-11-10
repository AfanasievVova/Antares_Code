for number in range(5, 16):
    print(number)

sum_of_number = 0
for number in range(1, 11):
    sum_of_number = sum_of_number + number  # 55 # додати число 1 + 2 + 3 + 4 .. и так далее
print(sum_of_number)

guest = 15
portions = 0
for guest in range(1, 16, 2):  # гости обед
    portions += 1
print(portions)

sum_of_number = 0
for number in range(5, 15, 2):
    sum_of_number = sum_of_number + number
print(sum_of_number)

trees = ["oak", "maple", "birch", "pine", "willow", "cedar", "redwood"]
for tree in trees:
    print(tree)

initial_distance = 5
increment = 2
total_weeks = 10

result = []  # створюємо порожній список для збереження значень

for run in range(5, 25, 2):
    result.append(run)  # додаємо значення до списку
    initial_distance += increment
    increment += total_weeks

print(result)

count = 1

while count <= 10:
    print(count)
    count += 1

money = 100
price_per_product = 10
products_bought = 0

while money >= price_per_product:
    products_bought += 1
    money -= price_per_product


print(f"You bought {products_bought} products")

countdown_start = 11

while countdown_start >= 1:
    countdown_start += -1
    print(countdown_start)

countdown_start = 10

while countdown_start >= 0:
    countdown_start += -1
    print(countdown_start)

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

for fruit in fruits:
    if len(fruit) == 5:
        print(fruit)

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)


initial_distance = 5
increment = 2
total_weeks = 10

result = []
for run in range(5, 25, 2):
    result.append(run)
    initial_distance += increment
    increment += total_weeks

print(result)

initial_distance = 5
increment = 2
total_weeks = 10

for week in range(total_weeks):
    print(initial_distance)  # Выводим расстояние для текущей недели
    initial_distance += increment  # Увеличиваем расстояние для следующей недели

tot = 0
for tots in range(1, 15):
    tots += 1
    print(tots)

print("================================")

tots = 0
for tot in range(5, 16):
    tot += tot + tot + tot
    print(tot)

print("=================================")
# Сумма чисел:
# Инициализируем переменную для хранения суммы
total_sum = 0

# Проходим по всем числам от 1 до 100
for number in range(1, 101):
    # Добавляем текущее число к общей сумме
    total_sum += number

# Выводим результат на экран
print("Сумма всех чисел от 1 до 100:", total_sum)

print("=====================================")

for i in range(2, 51, 2):
    print(i)

print("=======================")

for i in range(1, 11):
    result = i * 5
    print(result)

print("=============================")

for i in range(10, 0, -1):
    print(i)

print("=============================")

trees = ["oak", "maple", "birch", "pine", "willow", "cedar", "redwood"]
for tree in trees:
    print(tree)

print("==============================")

initial_distance = 5
increment = 2
total_weeks = 10

for run in range(5, 25, 2):
    initial_distance += increment
    increment += total_weeks
    print(run)

print("==========================")

for num in range(1, 111):
    if num % 2 == 0:
        print(num, "Четное")
    else:
        print(num, "Не четное")

for num in range(1, 16):
    num += 1
    print(num)

for num in range(5, 16):
    num += num + num + num
    print(num)

trees = ["oak", "maple", "birch", "pine", "willow", "cedar", "redwood"]
for tree in trees:
    print(tree)

initial_distance = 5
increment = 2
total_weeks = 10

for run in range(5, 25, 2):
    initial_distance += increment
    increment += total_weeks
    print(run)

savings = 100
book_price = 20
books = 0

while savings >= book_price:
    savings -= book_price
    books += 1
    print(f"Books Bought: {books}. Money Left {savings}")

money = 100
price_per_product = 10
products_bought = 0

while money >= price_per_product:
    money -= price_per_product
    products_bought += 1
    print(f"You bought {products_bought} products")


count = 1

while count <= 10:
    print(count)
    count += 1

money = 100
price_per_product = 10
products_bought = 0

while money >= price_per_product:
    money -= price_per_product
    products_bought += 1

# Після завершення циклу виводимо підсумкове повідомлення
print(f"You bought {products_bought} products")


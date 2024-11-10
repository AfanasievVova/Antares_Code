magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can`t wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")


pizza = ['margarita', 'Americano', '4 cheeses']
for pizzas in pizza:
    print(f"{pizzas.title()}. I like pizza")
    print(f"{pizzas.title()}. I really love pizza\n")


dog = ['Spitz', 'Sheep dog', 'dachshund']
for dogs in dog:
    print(f"{dogs.title()}, a dog would make a great pet!")
    print(f"{dogs.title()}, any of these animals would make a great pet!\n")

# ====================================================================================================

for value in range(1, 6):
    print(value)


list_num = list(range(2, 11, 2))
print(list_num)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sum(digits))


squares = [value ** 2 for value in range(1, 11)]
print(squares)


for value in range(1, 21):
    print(value)


milion = range(1, 1000001)
print(min(milion))
print(max(milion))
print(sum(milion))


for num in range(0, 21, 2):
    print(num)


list_num = [num for num in range(3, 31, 3)]
print(list_num)


cube = [value ** 3 for value in range(1, 11)]
print(cube)

cube = []
for value in range(1, 11):
    cubes = value ** 3
    cube.append(cubes)

print(cube)


def number(num1, num2):
    cube = []
    for i in range(len(num1)):
        cube.append(num1[i] + num2[i])
    return cube


print(number([110, 10, 10], [10, 56, 7889]))

players = ['charles', 'martin', 'michiel', 'florence', 'eli']
print(players[2:])

player = ['charles', 'martin', 'michiel', 'florence', 'eli']

print("Here are the first three players on my tame")
for players in player[:3]:
    print(players.title())


hot_dog = ['hot_dog', 'hot_dog_1', 'hot_dog_2', 'hot_dog_3']
for hot_dogs in hot_dog[:2]:
    print(hot_dogs)


def number(num1, num2):
    result_list = []
    for i in range(len(num1)):
        result_list.append(num1[i] * num2[i])
    return result_list


print(number([10, 30, 48], [56, 89, 45]))

result = ['b', 'm', 'w']
for results in result:
    print("Hello BMW cars!")
    print(results)


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("cake")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend`s favorite foods are:")
print(friend_foods)


massage_1 = ["The first three item in the list are:"]
massage_bro = massage_1[:]

print("Three items from the middle of the list are:")
print(massage_1)

print("\nThe last three items in the list are:")
print(massage_bro)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200, 750)
for dimension in dimensions:
    print(dimension)


foods = ("Pasta", "суп", "борщ", "риба", "м'ясо")
for food in foods:
    print(food)

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'pasta':
    print("Hold the anchovies!")

car = 'subaru'
print(car == 'subaru3')

age = 19
if age > 18:
    print("You are old enough to vote!")

age = float(input())
if age >= 18:
    print("Your are old enough to vote!")
    print("Have you registered to vote yet!")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

alien_color = ['green', 'yellow', 'red']

if alien_color == "green":
    print("Yes 5 bales")
elif alien_color == "yellow":
    print("Yes 10 bales")
else:
    print("Yes 15 bales")


age = float(input())
if age < 2:
    print("Це немовля")
elif age < 4:
    print("Це малюк")
elif age < 13:
    print("Дитина")
elif age < 20:
    print("Підліток")
elif age < 65:
    print("Дорослий")

favorite_fruits = ["banana", "mango", "mandarin", "apple", "pomidor"]

if "banana" in favorite_fruits:
    print("You really like bananas!")
if "mango" in favorite_fruits:
    print("You really like mango!")
if "mandarin" in favorite_fruits:
    print("You really like mandarin!")
if "egg" in favorite_fruits:
    print("You really like eggs!")
if "apple" in favorite_fruits:
    print("You really like apple")

# ============================= Словник
# ================================
# =================================
# ============================


alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}

new_alien_0 = alien_0['points']
print(f"You just earned {new_alien_0} points!")

alien_1 = {'color': 'green', 'points': 5}
print(alien_1)

alien_1['x_position'] = 25
alien_1['y_position'] = 0
print(alien_1)

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(favorite_languages['jen'])

point_value = favorite_languages.get('point', 'No point value assigned.')
print(point_value)
print("Спасибо что вы были в нашом опитуване")

my_bro = {
    'name': 'Kir',
    'last_name': 'None',
    'age': '14',
    'city': "Warshaw"
}

print(my_bro)

name_number = {
    'num_90': 'Kir',
    'num_10': 'Edward',
    'num_234': 'Svetlana',
    'num_2562': 'Nestor',
}

for number, name in name_number.items():
    print(f"{number}, bro number or name {name.title()}")


user_0 = {
    'user_name': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


english = {
    'American': 'English'
}

for english_1928 in english.keys():
    print(english_1928)

favorite_languages = {
    'jen': '',
    'Sarah': 'C',
    'Edward': '',
    'Phil': 'Python'
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

for language in set(favorite_languages.values()):
    print(language.title())

reki = {
    'null': 'american',
    'nill': 'egipt',
    'nilssd': 'Mexico'
}

for rekis in reki:
    print()
    print(rekis)

alien = {'speed': 'normal', 'x_position': '23'}

if alien['speed'] == 'slow':
    print("Yes speed normal")
else:
    print("sorry bro bat it this speed not normals")

def hello(world):
    return world


print(hello("Hello, world!"))
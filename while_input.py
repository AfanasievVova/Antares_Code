prompt = "hello, world!"
prompt += "\nHello bro"
name = input(prompt)
print(f"\nHello, {name}")

ages = "You age: "
age = int(input(ages))


cars = input("Name car: ")
print(f"Let me see if I can find you a {cars.title()}")



current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me"
prompt += "\n Enter"
massage = ""
while massage != 'quit':
    massage = input(prompt)

    if massage == 'quit':
        active = False
    else:
        print(massage)

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I`d love to go to {city.title()}!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)


pizza_ingredient = f"\npeperoni, american"
pizza_ingredient += "\nThe enter: "
massage = " "
while pizza_ingredient != 'quit':
    massage = input(pizza_ingredient)
    if pizza_ingredient != 'quit':
        break
    print(pizza_ingredient)

p = "\nHello my friend"
p += "\nEnter: "
massage = ""
while massage != 'quit':
    massage = input(p)
    if massage == 'quit':
        break
    print(massage)


def get_age_ticket():
    your_age = "Your age: "
    while age_count <= 12:
        age_count = int(input(your_age))
        if age_count <= 3:
            return "Cost ticket 0$"
        if age_count <= 6:
            return "Cost ticket 10$"
        if age_count <= 12:
            return "Cost ticket 15$"


print(get_age_ticket())



unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

def create_list(a, b):
    return list(range(a, b + 1))


a = 1
b = 4
print(create_list(a, b))

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("which mountain would you like to climb someday")

    responses[name] = response

    repeat = input("Would you like to let another person respond (Yes / No)")

    if repeat == 'No':
        polling_active = False

print("\n----Poll Results----")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")


Temperatur = 18

if Temperatur < 10:
    print("Temperatur is less than 10")

money = 500
book_price = 400
if money >= book_price:
    print("I can  buy the book ")

person_age = 25

if person_age >= 18:
    print("You can vote")

age = 21
if age < 19:
    print("Welcome")
else:
    print("Sorry Leave")


person_age = 15
if person_age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

age = 18
if age > 15:
    print("You can buy beer")
else:
    print("Ypu cannot buy beer")
#  Write code here


film_rating = 16
g = 13
pg = 9
pg_13 = 19

if film_rating > g:
    print("Suitable for all ages.")
if film_rating > pg:
    print("Parental guidance suggested.")
if film_rating < pg-13:
    print("Suitable for children aged 13 and older")
else:
    print("Sorry not age 18")

film_rating = "G"

if film_rating == "G":
    print("Suitable for all ages.")
if film_rating == "PG":
    print("Parental guidance suggested.")
if film_rating == "PG-13":
    print("Suitable for children aged 13 and older.")
else:
    print("Rating not recognized.")

film_rating = "G"

if film_rating == "G":
    print("Suitable for all ages.")
if film_rating == "PG":
    print("Parental guidance suggested.")
if film_rating == "PG-13":
    print("Suitable for children aged 13 and older.")

# Git

film_rating = "G"

rating_messages = {
    "G": "Suitable for all ages.",
    "PG": "Parental guidance suggested.",
    "PG-13": "Suitable for children aged 13 and older."
}

if film_rating in rating_messages:
    print(rating_messages[film_rating])


friends = 5
food = 8

if friends <= food:
    print("You are friend")
elif friends > food:
    print("You are not friend")
else:
    print("Not friends Not food")



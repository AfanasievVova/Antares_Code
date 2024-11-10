def get_lists_sum(ls1, ls2):
    result_sum = sum(ls1) + sum(ls2)
    return result_sum


print(get_lists_sum([1, 2], [3, 4]))


def combine_lists(ls1, ls2):
    result_list = []
    for i in range(len(ls1)):
        result_list.append(ls1[i] + ls2[i])
    return result_list


print(combine_lists([1, 2, 5], [3, 6, 1]))


def sum_two_lists(list1, list2):
    result_list = []
    for n in range(len(list1)):
        result_list.append(list1[n] + list2[n])
    return result_list


print(sum_two_lists([1, 2, 3, 4], [5, 6, 7, 8]))


def remove_vowels(document):
    vowels = "aeiouyAEIOUY"
    remove = ""
    for char in document:
        if char not in vowels:
            remove += char
        return remove


print(remove_vowels("captain"))
print(remove_vowels("I like my boss"))
print(remove_vowels("350 euro"))


def make_stickers(details_count, robot_part):
    return [f"{robot_part} detail #{i + 1}" for i in range(details_count)]


# Приклад використання:
stickers = make_stickers(3, "Body")
print(stickers)


def car(car1_det, car2_car):
    return [f"{car2_car} detali #{i + 1}" for i in range(car1_det)]


cars = car(3, "Body")
print(cars)


def double_power(current_powers):
    doubled_pow = []
    for num in current_powers:
        doubled_pow.append(num * 2)
    return doubled_pow

print(double_power([100, 150, 200, 220]))

def get_location(coordinates, commandss):
    x, y = coordinates

    for commands in commandss:
        if commands == "forward":
            y += 1
        elif commands == "back":
            y -= 1
        elif commands == "right":
            x += 1
        elif commands == "right":
            x -= 1
    return x, y

print(get_location([0, 0], ["forward", "right"]))
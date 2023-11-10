def pizza_size():
    result = 0
    print("""
    ===Available on the Order List===
        1. Large size
        2. Medium size
        3. Small size
    """)
    order_selection = input("Kindly place your preferred box size: ")
    if order_selection == "1":
        result = 10

    elif order_selection == "2":
        result = 6

    elif order_selection == "3":
        result = 4
    else:
        return pizza_size()
    return result


print(pizza_size())


def hunger_level():
    result = " "
    print("""
    ====Hunger Level of Quests
    1. Super hungry eaters
    2. Normal hunger level eaters
    3. Classic eaters
    """)
    hunger = input("Kindly select an option: ")
    if hunger == "1":
        result = 4
    elif hunger == "2":
        result = 2
    elif hunger == "3":
        result = 1
    else:
        hunger_level()
    return result


print(hunger_level())


def total_number_of_slices():
    if pizza_size() == "1" and hunger_level() == "1":
        total_number_of_slices = 

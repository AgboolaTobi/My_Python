def largest_element(array):
    largest = array[0]
    for count in array:
        if count > largest:
            largest = count
    return largest


def reverse_list(my_array):
    left_side = 0
    right_side = len(my_array) - 1
    while left_side < right_side:
        toby = my_array[left_side]
        my_array[left_side] = my_array[right_side]
        my_array[right_side] = toby
        left_side += 1
        right_side -= 1

    return my_array


# the reverse method could to be shorter


def check_element(my_array, to_check):
    for count in my_array:
        if count == to_check:
            return True
    return check_element()


# just return the expression, it will evaluate to true or false
#  Done sir

def odd_position_element(my_array):
    oddly_positined = []
    for element in range(1, len(my_array), 2):
        oddly_positined.append(my_array[element])
    return oddly_positined


def even_position_element(my_array):
    evenly_positined = []
    for element in range(0, len(my_array), 2):
        evenly_positined.append(my_array[element])
    return evenly_positined


def running_total(my_array):
    total = 0
    name = " "
    for i in range(0, len(my_array)):
        total = total + my_array[i]
        collect_total = f"{total}"
        name += collect_total + " "
    return name


# what are you trying to do here?
# if it to get the total, you dont need the range function, just loop through

# Trying to get the total at each count sir and not just the final total

def is_palindrome(my_array):
    for element in range(0, int(len(my_array) / 2)):
        if my_array[element] == my_array[len(my_array) - element - 1]:
            return True
        else:
            False
    return is_palindrome()


# can u refactor this and return the final expression will give true or false
# Done sir

def sum_for_loop(my_array):
    sum_total = 0
    for i in len(my_array):
        sum_total = sum_total + my_array[i]
    return sum_total


# just loop through without using the range function
# Done sir

def sum_while_loop(my_array):
    sum_total = 0
    count = 0
    while count < len(my_array):
        sum_total = sum_total + my_array[count]
        count += 1
    return sum_total


def concatenation_of_lists(my_array1, my_array2):
    my_array = my_array1 + my_array2
    return my_array


# after we discuss list in class, you will refactor this into one line... lol
#  Done sir(Thanks sir !)

def alternate_combination(myArray1, myArray2):
    merged_array = []
    min_len = min(len(myArray1), len(myArray2))

    for i in range(min_len):
        merged_array.append(myArray1[i])
        merged_array.append(myArray2[i])

    merged_array += myArray1[min_len:] + myArray2[min_len:]
    return merged_array


def digits_to_list(my_array):
    str(my_array)
    int_array = []
    for i in range(len(my_array)):
        int_array.append(int(my_array[i]))
    return int_array


my_array1 = [1, 2, 3, 4]
my_array2 = [6, 7, 9, 8]

array = my_array1 + my_array2
print(array)

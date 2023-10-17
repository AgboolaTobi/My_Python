def reverse(tuple1):
    reversed_tuple = ()
    for i in range(len(tuple1) - 1, -1, -1):
        reversed_tuple += (tuple1[i],)
    return reversed_tuple


def singleton(tuple1):
    single = ()
    if len(tuple1) == 1:
        for i in tuple1:
            single = i,
    return single


def unpacking(tuple1):
    created_tuple = ()
    for i in range(-1, len(tuple1)):
        created_tuple += (tuple1[i], tuple1[0])
        return created_tuple


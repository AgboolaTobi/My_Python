def reverse_tuple(tuple1):
    new_tuple = ()
    for i in range(len(tuple1) - 1, -1, -1):
        new_tuple += (tuple1[i],)
    return new_tuple

def flatten(iterable):
    new_list = []
    for i in iterable:
        recursividad(i, new_list)

    return new_list


def recursividad(iterable, new_list):
    if type(iterable) is list:
        for i in iterable:
            if type(i) is list:
                recursividad(i, new_list)
                continue
            if i is not None:
                new_list.append(i)
    else:
        if iterable is not None:
            new_list.append(iterable)


if __name__ == "__main__":
    print("Result: ", flatten([[[]]])) #[]
    print("Result: ", flatten([0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2])) #[0, 2, 2, 3, 8, 100, 4, 50, -2]
    print("Result: ", flatten([0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2])) #[0, 2, 2, 3, 8, 100, -2]
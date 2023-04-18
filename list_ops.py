def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_list = []
    for i in lists:
        new_list += i
    return new_list


def filter(function, list):
    new_list = []
    for i in list:
        if function(i):
            new_list.append(i)
    return new_list


def length(list):
    count = 0
    for i in list:
        count += 1
    return count


def map(function, list):
    new_list = []
    for i in list:
        new_list.append(function(i))
    return new_list


def foldl(function, list, initial):
    accumulator = initial
    for i in list:
        accumulator = function(accumulator, i)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    for i in range(len(list) - 1, -1, -1):
        accumulator = function(list[i], accumulator)
    return accumulator


def reverse(list):
    list = list[::-1]
    return list


if __name__ == "__main__":
    print(append([1, 2], [2, 3, 4, 5])) #[1, 2, 2, 3, 4, 5]
    print(concat([[[1], [2]], [[3]], [[]], [[4, 5, 6]]])) #[[1], [2], [3], [], [4, 5, 6]]
    print(filter(lambda x: x % 2 == 1, [1, 2, 3, 5])) #[1, 3, 5]
    print(map(lambda x: x + 1, [1, 3, 5, 7])) #[2, 4, 6, 8]
    print(foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5)) #15
    print(foldr(lambda x, y: x + y, ["e", "x", "e", "r", "c", "i", "s", "m"], "!")) #exercism!
    print(reverse(["xyz", 4.0, "cat", 1])) #[1, "cat", 4.0, "xyz"]
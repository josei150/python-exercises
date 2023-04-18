grains_in_square = []


def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grain = 1
    for i in range(1, 65):
        grains_in_square.append(grain)
        grain *= 2
    return grains_in_square[number - 1]


def total():
    count_grains = 0
    for i in grains_in_square:
        count_grains += i
    return count_grains

if __name__ == "__main__":
    print(square(64))
    print(total())
    print(129127208515966861305 / total())
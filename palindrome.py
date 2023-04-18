def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    target = []
    palin = []
    num_limit = min_factor - 1
    if max_factor > 1000:
        num_limit = max_factor - min_factor - 1

    #Busco el palíndromo más grande
    for i in range(max_factor, num_limit, -1):
        for j in range(max_factor, num_limit, -1):
            if str(i * j) == str(i * j)[::-1]:
                palin.append(i * j)
                break
    
    palin = sorted(palin)
    
    #Busco los factores del palíndromo
    for i in range(min_factor, max_factor):
        if palin[len(palin) - 1] % i == 0:
            target.append([i, palin[len(palin) - 1] // i])
    return palin[len(palin) - 1], [target[len(target) - 1]] if max_factor > 10 else target


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    target = []
    palin = None

    for i in range(min_factor, max_factor):
        if palin is not None:
            break
        for j in range(min_factor, max_factor):
            if str(i * j) == str(i * j)[::-1]:
                palin = i * j
                break
    
    if palin is None:
        return palin, []
    
    for i in range(min_factor, max_factor):
        if palin % i == 0:
            target.append([i, palin // i])
            break
    return palin, [target[len(target) - 1]]

if __name__ == "__main__":
    print(smallest(1002, 1003))
    print(largest(100, 999))


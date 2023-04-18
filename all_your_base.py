def rebase(input_base, digits, output_base):
    digits = digits[::-1]
    decimal_digits = 0
    finalDigit = []
    dividendo = 0
    divisor = 0
    
    if input_base <= 1:
        raise ValueError("input base must be >= 2")

    if output_base <= 1:
        raise ValueError("output base must be >= 2")

    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    for index, value in enumerate(digits):
        # print("Index: " + str(index) + " - Value: " + str(value))
        # print((value * input_base**index))
        decimal_digits += (value * input_base**index)

    if decimal_digits == 0:
        return [0]

    print("Decimal ", decimal_digits)

    # decimal_digits = list(str(decimal_digits))
    # decimal_digits = [int(i) for i in decimal_digits]

    dividendo = decimal_digits
    divisor = output_base

    while dividendo >= 1:
        
        #print(dividendo, divisor)

        if dividendo % divisor == 0:
            finalDigit.append(0)
        else:
            finalDigit.append(dividendo % divisor)
        
        dividendo = dividendo // divisor

    finalDigit = finalDigit[::-1]

    return finalDigit


if __name__ == "__main__":
    # rebase(2, [1], 10), [1]
    print("Base 2 " + str(rebase(2, [1, 0, 1, 0, 1, 0], 10)))
    print("Base 10 " + str(rebase(10, [4, 2], 2)))
    print("Base 3 " + str(rebase(3, [1, 1, 2, 0], 16)))
    print("Base 16 " + str(rebase(16, [2, 10], 3)))
    print("Base 97 " + str(rebase(97, [3, 46, 60], 73))) # 28227 + 4462 + 60
    print(rebase(2, [], 10))
    print(rebase(10, [0], 2), [0])
    print(rebase(10, [0, 0, 0], 2))
    print(rebase(7, [0, 6, 0], 10))
    print(rebase(1, [0], 10))
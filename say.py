def say(number):
    """
    Given a number from 0 to 999,999,999,999, spell out that number in English.
    """
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    
    text_numbers_data = {
        "0" : "zero",
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine",
        "10" : "ten",
        "11" : "eleven",
        "12" : "twelve",
        "13" : "thirteen",
        "14" : "fourteen",
        "15" : "fifteen",
        "16" : "sixteen",
        "17" : "seventeen",
        "18" : "eighteen",
        "19" : "nineteen",
        "20" : "twenty",
        "30" : "thirty",
        "40" : "forty",
        "50" : "fifty",
        "60" : "sixty",
        "70" : "seventy",
        "80" : "eighty",
        "90" : "ninety",
    }

    if number < 21:
        return text_numbers_data[str(number)]

    digits = []
    residue = number
    words_each_three_numbers = ["", "thousand", "million", "billion"]
    result = []
    trio_numbers = []
    trio_numbers_result = []
    
    while residue > 0:
        digits.append(residue % 1000)
        #print(f'{residue=}')
        residue //= 1000

    #digits = list(reversed(digits))
    #print(f'{digits=}')

    
        

    for digit in digits:
        trio_numbers.append(str(digit))
    
    for index, value in enumerate(trio_numbers):
        if len(value) == 2:
            trio_numbers[index] = '0' + trio_numbers[index]

    #print(f'{trio_numbers=}')

    for trio in trio_numbers:
        text = ""
        if len(trio) == 3:
            text += text_numbers_data[trio[0]] + " hundred "
            if trio[1:] in text_numbers_data:
                text += text_numbers_data[trio[1:]]
                trio_numbers_result.append(text)
                continue
            else:
                if trio[1] == "0":
                    text += text_numbers_data[trio[1]] + "-" + text_numbers_data[trio[2]]
                    trio_numbers_result.append(text)
                    continue
                else:
                    text += text_numbers_data[trio[1] + "0"] + "-" + text_numbers_data[trio[2]]
                    trio_numbers_result.append(text)
                    continue
        if trio[0:] in text_numbers_data.keys():
            text += text_numbers_data[trio[0:]]
            trio_numbers_result.append(text)
            continue
        else:
            #print(f'{trio=}')
            if trio[1] == "0":
                    text += text_numbers_data[trio[1]] + "-" + text_numbers_data[trio[2]]
                    trio_numbers_result.append(text)
                    continue
            else:
                text += text_numbers_data[trio[1] + "0"] + "-" + text_numbers_data[trio[2]]
                trio_numbers_result.append(text)
                continue
    
    trio_numbers_result = list(reversed(trio_numbers_result))
    #print(list(reversed(trio_numbers_result)))

    for index, digit in enumerate(digits):
        result.append(words_each_three_numbers[index])
        result.append(str(digit))

    result = list(reversed(result))
    counter = 0
    for index, value in enumerate(result):
        if value.isnumeric():
            result[index] = trio_numbers_result[counter]
            counter += 1

    return (" ".join(result)).replace("zero hundred ", "").replace("zero-zero", "").replace("zero", "").replace("  thousand", "").replace("  million", "").strip()


if __name__ == "__main__":
    print(say(1000000))
    print(say(987654321123))
    print(say(1002345))
def say(number):
    """
    Given a number from 0 to 999,999,999,999, spell out that number in English.
    """
    digits = []
    residue = number
    words_each_three_numbers = ["", "thousand", "million", "billion"]
    result = []
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
    trio_numbers = []
    trio_numbers_result = []

    while residue > 0:
        digits.append(residue % 1000)
        residue //= 1000

    #digits = list(reversed(digits))

    for digit in digits:
        trio_numbers.append(str(digit))

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
            if trio[1] == "0":
                    text += text_numbers_data[trio[1]] + "-" + text_numbers_data[trio[2]]
                    trio_numbers_result.append(text)
                    continue
            else:
                text += text_numbers_data[trio[1] + "0"] + "-" + text_numbers_data[trio[2]]
                trio_numbers_result.append(text)
                continue

    print(list(reversed(trio_numbers_result)))

    for index, digit in enumerate(digits):
        result.append(words_each_three_numbers[index])
        result.append(str(digit))

    return list(reversed(result))


if __name__ == "__main__":
    print(say(1234567890))
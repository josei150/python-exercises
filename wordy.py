import re

def answer(question):
    question_list = re.split("[ ?]", question)
    operation = []
    total = None

    if 'cubed' in question_list or 'Who' in question_list:
        raise ValueError("unknown operation")

    if not re.search('\w+ \w+ -?\d+\?', question) and not re.search('\w+ \w+ -?\d+ \w+ -?\d+.*\?', question) or re.search('\w+ \w+ -?\d+ -?\d+ \w+ -?\d+.*\?', question) or re.search('\w+ \w+ -?\d+ \w+ -?\d+ -?\d+.*\?', question):
        raise ValueError("syntax error")
    
    if 'plus' not in question_list and 'minus' not in question_list and 'multiplied' not in question_list and 'divided' not in question_list and not re.search('What is \d+?', question):
        raise ValueError("unknown operation")

    
    
    for i in question_list:
        if re.search("-\d+", i):
            operation.append(int(i))
        if i.isnumeric():
            operation.append(int(i))
        if i == 'plus':
            operation.append(i)
        if i == 'minus':
            operation.append(i)
        if i == 'multiplied':
            operation.append(i)
        if i == 'divided':
            operation.append(i)

    
    total = operation[0]

    for index, value in enumerate(operation):
        if value == 'plus':
            total = plus(total, operation[index + 1])
        if value == 'minus':
            total = minus(total, operation[index + 1])
        if value == 'multiplied':
            total = multiplied(total, operation[index + 1])
        if value == 'divided':
            total = divided(total, operation[index + 1])

    return total


def plus(a, b):
    try:
        return a + b
    except TypeError:
        raise ValueError("syntax error")


def minus(a, b):
    try:
        return a - b
    except TypeError:
        raise ValueError("syntax error")


def multiplied(a, b):
    try:
        return a * b
    except TypeError:
        raise ValueError("syntax error")


def divided(a, b):
    try:
        return a / b
    except TypeError:
        raise ValueError("syntax error")


if __name__ == "__main__":
    print(answer("What is 3 plus 2 multiplied by 3?"))
    print(answer("What is 3 plus 2 multiplied by 3 divided by 5?"))
    print(answer("What is 2 multiplied by 3?"))

    
    
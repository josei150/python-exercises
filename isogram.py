import re

def is_isogram(string):
    sentence = re.split("[][-]?", string.lower())
    phrase = ''

    for i in sentence:
        phrase += i


    print(len(phrase), phrase)
    print(len(set(phrase)), set(phrase))

if __name__ == "__main__":
    print(is_isogram("Emily Jung Schwartzkopf"))
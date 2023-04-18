import re

def is_pangram(sentence):
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    sentence = re.split("[\W_?\D]", sentence.lower())
    phrase = ''

    for i in sentence:
        phrase += i

    print(phrase)

    return len(set(phrase)) == len(letters)



if __name__ == "__main__":
    print(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"))
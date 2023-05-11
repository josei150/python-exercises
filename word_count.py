import re

def count_words(sentence):
    # word_list = sentence.split()
    sentence = sentence.lower()
    word_list = re.split("[\s ,_-]", sentence)

    depured_words = []
    words = {}

    for i in word_list:
        depured_words.append("".join(re.findall("[\w\'*]", i)))
    
    print(f"{depured_words=}")


    for i, value in enumerate(depured_words):
        if len(value) >= 1:
            depured_words[i] = depured_words[i].strip("', \"")#depured_words[i][1:]

            # if depured_words[i][0] == "'":
            # if depured_words[i][len(depured_words[i]) - 1] == "'":
            #     depured_words[i] = depured_words[i][:len(depured_words[i]) -1]

    print(f"{depured_words=}")

    for index, value in enumerate(depured_words):
        words[value] = depured_words.count(value)

    if "" in words:
        del words[""]

    return words

if __name__ == "__main__":
    print(count_words("''hey''"))
import re

# 00001 = wink
# 00010 = double blink
# 00100 = close your eyes
# 01000 = jump
# 10000 = Reverse the order of the operations in the secret handshake.

def commands(binary_str):
    secret = ["Reverse", "jump", "close your eyes", "double blink", "wink"]
    binary = re.split("", binary_str)
    code = []

    for index, value in enumerate(binary):
        if value == '':
            continue
        if value == '1' and index != 1:
            code.append(secret[index - 1])

    code.reverse()

    if binary_str[0] == '1':
        code.reverse()
    
    return code



if __name__ == "__main__":
    print(commands("00011"))
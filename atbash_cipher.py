import re

PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    code = ''
    clean_text = re.split('[ ,.]', plain_text.lower())
    plain_text_lower = ''
    count = 0

    for i in clean_text:
        plain_text_lower += i

    for i in plain_text_lower:
        
        if i.isnumeric():
            code += i
        else:
            code += CIPHER[PLAIN.index(i)]
        
        count += 1
        
        if count % 5 == 0:
            code += ' '

    if code[len(code) - 1] == ' ':
        code = code[:len(code) - 1]
    return code


def decode(ciphered_text):
    code = ''
    clean_text = re.split('[ ,.]', ciphered_text.lower())
    plain_text_lower = ''
    
    for i in clean_text:
        plain_text_lower += i

    for i in plain_text_lower:
    
        if i.isnumeric():
            code += i
            continue
        code += PLAIN[CIPHER.index(i)]
    
    return code



if __name__ == "__main__":
    print(encode("The quick brown fox jumps over the lazy dog."))
    #print(decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"))
    #gvhgr mt123 gvhgr mt
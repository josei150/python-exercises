def matrix_code(message, rails):
    arreglo = [["*" for i in range(len(message))] for j in range(rails)]
    count = 0
    on_off = 0
    while count < len(message):
        if on_off == 0:
            for i in range(rails):
                if count >= len(message):
                    continue
                arreglo[i][count] = message[count]
                print("Positivos", i , count)
                count += 1
            on_off = 1
        else:
            for i in range(rails-2, 0, -1):
                if count >= len(message):
                    continue
                arreglo[i][count] = message[count]
                print("Negativos", i , count)
                count += 1
            on_off = 0
    
    return arreglo

def encode(message, rails):
    
    matrix = matrix_code(message, rails)
    code = ""

    for i in matrix:
        for j in i:
            if j == "*":
                continue
            else:
                code += j
    
    return code

def decode(encoded_message, rails):
    matrix = matrix_code(encoded_message, rails)

    code = ""
    count = 0
    for i, value in enumerate(matrix):
        for j, valor in enumerate(value):
            if valor == "*":
                continue
            else:
                matrix[i][j] = encoded_message[count]
                count += 1
    
    count = 0
    on_off = 0
    while count < len(encoded_message):
        if on_off == 0:
            for i in range(rails):
                if count >= len(encoded_message):
                    continue
                code += matrix[i][count]
                print("Positivos", i , count)
                count += 1
            on_off = 1
        else:
            for i in range(rails-2, 0, -1):
                if count >= len(encoded_message):
                    continue
                code += matrix[i][count]
                print("Negativos", i , count)
                count += 1
            on_off = 0

    print(matrix)
    
    return code


if __name__ == "__main__":
    #print(encode("WEAREDISCOVEREDFLEEATONCE", 3)) #WECRLTEERDSOEEFEAOCAIVDEN
    # print(encode("XOXOXOXOXOXOXOXOXO", 2)) #XXXXXXXXXOOOOOOOOO
    # print(encode("EXERCISES", 4)) #ESXIEECSR
    #print(encode("WEAREDISCOVEREDFLEEATONCE", 3))#WECRLTEERDSOEEFEAOCAIVDEN
    print(decode("EIEXMSMESAORIWSCE", 5))#EXERCISMISAWESOME

    
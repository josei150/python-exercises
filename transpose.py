def transpose(lines):
    lines = lines.split("\n")
    text_transpose = []
    greater = 0
    # print(lines)
    #Contamos cual string tiene más caracteres
    for i in lines:
        if len(i) > greater:
            greater = len(i)

    # print(f"greater: {greater}")
    
    #Agrego los espacios
    for i in range(greater):
        text_transpose.append('')

    #print(f"Lines: {lines} - text transpose: {text_transpose}")

    for i, v in enumerate(lines):
        #print(f"i: {i} - v: {v}")
        for index, value in enumerate(v):
            # print(f"index: {index} - value: {value}")
            
            if len(v) > len(lines[i - 1]) and index > len(lines[i - 1]) - 1:
                text_transpose[index] += (' ' * (i))
                # print(text_transpose)
            text_transpose[index] += value
    
    #print(f"Lines: {lines} - text transpose: {text_transpose}")

    # for i, text in enumerate(text_transpose):
    #     aux = len(text)
    #     if aux > len(text_transpose):
    #         aux -= 1
    #     if len(text_transpose[i + 1]) > len(text):
    #         print("entramos")
    #         text = text.split('')
    #         indice = text.index(" ")
    #         text.pop(indice)
    #         text_transpose[i] = str(ext)

    return "\n".join(text_transpose)
    # return text_transpose


if __name__ == "__main__":
    #print(transpose("\n".join(["The fourth line.", "The fifth line."])))
    #print(transpose("\n".join(["The first line.", "The second line."])))
    #print(transpose("\n".join(["The longest line.", "A long line.", "A longer line.", "A line."])))
    print(transpose("\n".join(["T", "EE", "AAA", "SSSS", "EEEEE", "RRRRRR"])))
    #print("\n".join(["TEASER", " EASER", "  ASER", "   SER", "    ER", "     R"]))
    # print(transpose("\n".join(["11", "2", "3333", "444", "555555", "66666"])))
    
    print(transpose("\n".join(["The longest line.", "A long line.", "A longer line.", "A line."])))

    # print(transpose("\n".join(["The first line.", "The second line."])))
    # print("\n".join(["123456", "1 3456", "  3456", "  3 56", "    56", "    5"]))


    #print(transpose("\n".join(["ABC", "123"])))
    #print(transpose("\n".join([])))
    
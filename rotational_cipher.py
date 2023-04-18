def rotate(text, key):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cypher = ''

    for i in text:
        if i == i.upper():
            if i.lower() in plain:
                index_text = plain.index(i.lower())
                
                if (index_text + key) > (len(plain) - 1):
                    cypher += plain[index_text + key - (len(plain))].upper()
                else:
                    cypher += plain[index_text + key].upper()
            else:
                cypher += i
        else:
            if i in plain:
                index_text = plain.index(i)
                
                if (index_text + key) > (len(plain) - 1):
                    cypher += plain[index_text + key - (len(plain))]
                else:
                    cypher += plain[index_text + key]
            else:
                cypher += i


    return cypher

if __name__ == "__main__":
    print(rotate("O M G", 5))
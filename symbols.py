def is_paired(input_string):
    simbol = {"parentesis_izq": 0,
        "parentesis_der": 0,
        "corchete_izq": 0,
        "corchete_der": 0,
        "llave_izq": 0,
        "llave_der": 0}
    
    
    for i, value in enumerate(input_string):
        if value == '(':
            simbol["parentesis_izq"] += 1
        if value == ')':
            if input_string[i - 1] == '[' or input_string[i - 1] == '{':
                return False
            simbol["parentesis_der"] += 1
        if value == '[':
            simbol["corchete_izq"] += 1
        if value == ']':
            if input_string[i - 1] == '(' or input_string[i - 1] == '{':
                return False
            simbol["corchete_der"] += 1
        if value == '{':
            simbol["llave_izq"] += 1
        if value == '}':
            if input_string[i - 1] == '(' or input_string[i - 1] == '[':
                return False
            simbol["llave_der"] += 1
        if simbol["parentesis_der"] > simbol["parentesis_izq"] or simbol["corchete_der"] > simbol["corchete_izq"] or simbol["llave_der"] > simbol["llave_izq"]:
            return False
        
    print(simbol)
    if simbol["parentesis_izq"] == simbol["parentesis_der"] and simbol["corchete_izq"] == simbol["corchete_der"] and simbol["llave_izq"] == simbol["llave_der"]:
        return True

    return False


if __name__ == "__main__":
    print(is_paired("[({]})"))
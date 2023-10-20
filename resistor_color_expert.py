def resistor_label(colors):
    bands = {
        "Black": "0",
        "Brown": "1",
        "Red": "2",
        "Orange": "3",
        "Yellow": "4",
        "Green": "5",
        "Blue": "6",
        "Violet": "7",
        "Grey": "8",
        "White": "9",
    }

    tolerances = {
        "Grey" : "0.05%",
        "Violet" : "0.1%",
        "Blue" : "0.25%",
        "Green" : "0.5%",
        "Brown" : "1%",
        "Red" : "2%",
        "Gold" : "5%",
        "Silver" : "10%",
    }

    num_of_bands = len(colors)
    total_value = ""

    if num_of_bands < 3:
        for color in colors:
            total_value += bands[color.capitalize()]
        return total_value + " ohms"
    
    if num_of_bands == 3:
        for index, color in enumerate(colors):
            if index < len(colors) - 1:
                total_value += bands[color.capitalize()]
            else:
                total_value += " ohms ±"
                total_value += tolerances[color.capitalize()]
        return total_value
    
    if num_of_bands < 6:
        invert_colors = colors[::-1]
        invert_value = []
        invert_nums = ""
        for index, color in enumerate(invert_colors):
            if index == 0:
                invert_value.append("±" + tolerances[color.capitalize()])
            elif index == 1:
                print(int(bands[color.capitalize()]))
                invert_nums += int(bands[color.capitalize()]) * "0"
            else:
                invert_nums += bands[color.capitalize()]
        test_K_M = int(invert_nums[::-1])
        print(test_K_M)
        if test_K_M < 1000:
            invert_nums = str(test_K_M) + " ohms"
        elif test_K_M < 1000000:
            invert_nums = str(test_K_M / 1000) + " kiloohms"
        elif test_K_M > 1000000:
            invert_nums = str(test_K_M / 1000000) + " megaohms"
        
            
        invert_value.append(invert_nums)
        total_value = " ".join(invert_value[::-1])
        return total_value.replace(".0 ", " ")

if __name__ == "__main__":
    print(resistor_label(["red"]))
    
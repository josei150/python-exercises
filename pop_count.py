def egg_count(display_value):
    binary = []
    residue = display_value
    counter_eggs = 0

    while residue != 0:
        if residue % 2 == 0:
            binary.append(0)
        else:
            binary.append(1)
        residue = residue // 2
    
    binary.reverse()

    for egg in binary:
        if egg == 1:
            counter_eggs += 1

    return counter_eggs

if __name__ == "__main__":
    print(egg_count(89))
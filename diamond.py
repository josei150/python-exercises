def rows(letter):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    position_letter = alphabet.index(letter) + 1
    spaces_between_letters = position_letter * 2 - 3
    spaces_outside_letters = 0
    letters_selected = list(reversed(alphabet[:position_letter]))
    result = []

    if letter == "A":
        return ["A"]

    result.append((" " * spaces_outside_letters) + letters_selected[0] + (" " * spaces_between_letters) + letters_selected[0] + (" " * spaces_outside_letters))
    letters_selected.remove(letter)

    for i in letters_selected:
        spaces_outside_letters += 1
        spaces_between_letters -= 2
        if i != "A":
            print(f'{spaces_outside_letters=}')
            result.insert(0, (" " * spaces_outside_letters) + i + (" " * spaces_between_letters) + i + (" " * spaces_outside_letters))
            result.append((" " * spaces_outside_letters) + i + (" " * spaces_between_letters) + i + (" " * spaces_outside_letters))
        else:
            result.insert(0, (" " * spaces_outside_letters) + i + (" " * spaces_outside_letters))
            result.append((" " * spaces_outside_letters) + i + (" " * spaces_outside_letters))

    return result

if __name__ == "__main__":
    print(rows("C"))
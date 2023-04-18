import re

def is_valid(isbn):
    match = re.search("\d-\d{3,3}-\d{5,5}-[\dX]+", isbn)
    match_2 = re.search("\d{9,9}[\dX]+", isbn)
    
    ten = 0
    
    if isbn == '':
        return False

    if match_2:
        if len(match_2.group()) > 10:
            return False

    if isbn[len(isbn) - 1] == 'X':
        ten = 10

    if match or match_2:
        
        isbn = re.split("[\D]", isbn)
        count = 0
        decrement = 11
    
        numbers = ''

        for i in isbn:
            numbers += i

        for i in numbers:
            decrement -= 1
            count += (int(i) * decrement)

        if ten == 10:
            count += 10

        if count % 11 == 0:
            return True

    return False


if __name__ == "__main__":
    print(is_valid("98245726788"))
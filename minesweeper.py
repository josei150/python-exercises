def annotate(minefield):
    matrix = []
    matrix_string = []
    dimension = len(minefield[0])

    for value in minefield:
        if len(value) != dimension:
            raise ValueError("The board is invalid with current input.")

    for i in range(len(minefield)):
        matrix.append([])
        for j in range(len(minefield[i])):
            if minefield[i][j] == ' ':
                matrix[i].append(0)
                if j + 1 < len(minefield[i]): #miro a la derecha
                    if minefield[i][j + 1] == '*':
                        matrix[i][j] += 1
                if i + 1 < len(minefield): #miro hacia abajo
                    if minefield[i + 1][j] == '*':
                        matrix[i][j] += 1
                if j - 1 >= 0: #miro a la izquierda
                    if minefield[i][j - 1] == '*':
                        matrix[i][j] += 1
                if i - 1 >= 0: #miro hacia arriba
                    if minefield[i - 1][j] == '*':
                        matrix[i][j] += 1
                if j - 1 >= 0 and i - 1 >= 0: #miro a la izquierda-arriba
                    if minefield[i - 1][j - 1] == '*':
                        matrix[i][j] += 1
                if j + 1 < len(minefield[i]) and i - 1 >= 0: #miro a la derecha-arriba
                    if minefield[i - 1][j + 1] == '*':
                        matrix[i][j] += 1
                if j + 1 < len(minefield[i]) and i + 1 < len(minefield): #miro a la derecha-abajo
                    if minefield[i + 1][j + 1] == '*':
                        matrix[i][j] += 1
                if j - 1 >= 0 and i + 1 < len(minefield): #miro a la izquierda-abajo
                    if minefield[i + 1][j - 1] == '*':
                        matrix[i][j] += 1
                continue

            if minefield[i][j] == '*':
                matrix[i].append('*')
    
    
    for i in matrix:
        aux = ''
        for j in range(len(i)):
            if i[j] == 0:
                aux += ' '
            else:
                aux += str(i[j])
            
        matrix_string.append(aux)
    
    return matrix_string


if __name__ == "__main__":
    test_1 = ["   ", " * ", "*  "]
    test_2 = [" * * ", "  *  ", "  *  ", "     "]
    print(annotate(test_2))

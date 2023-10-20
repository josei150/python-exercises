def saddle_points(matrix):
    grid = {"row": 0, "column": 0}
    
    rows = []
    cols = []
    grid_options = []

    for index_r, row in enumerate(matrix):
        taller = matrix[index_r][0]
        smaller = matrix[index_r][0]
        for index_c, col in enumerate(row):
            print("Fila", index_r, "columna", index_c)
            print("Valor", col)
            if col > taller:
                taller = col
                rows.append({"row" : index_r, "column" : index_c, "value" : matrix[index_r][index_c]})
                print("Taller", taller)
            print(matrix[index_c][index_r])
            if matrix[index_c][index_r] < smaller:
                smaller = col
                cols.append({"row" : index_r, "column" : index_c, "value" : matrix[index_r][index_c]})
                print("smaller", smaller)

    #print(grid_options)
    for index, value in enumerate(rows):
        #print(smaller , grid_options)
        if value in cols:
            grid_options.append(value)
            
    c = zip(*matrix)
    return list(c)

if __name__ == "__main__":
    #print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]]))
    #print(saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]]))
    print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]]))
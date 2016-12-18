def checkio(matrix):
    length = len(matrix)
    print length
    for i in range(length):
        for j in range(length):
            if i + 4 <= length : 
                if matrix[i][j] ==  matrix[i + 1][j] == matrix[i + 2][j] == matrix[i + 3][j]:
                    return True
            if j + 4 <= length :
                if matrix[i][j] ==  matrix[i][j + 1] == matrix[i][j + 2] == matrix[i][j + 3]:
                    return True
            if i + 4 <= length and j + 4 <= length:
                if matrix[i][j] ==  matrix[i + 1][j + 1] == matrix[i + 2][j + 2] == matrix[i + 3][j + 3]:
                    return True
            if j - 3 >= 0 and i + 4 <=length :
                if matrix[i][j] ==  matrix[i + 1][j - 1] == matrix[i + 2][j - 2] == matrix[i + 3][j - 3]:
                    return True
    return False

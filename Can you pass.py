import numpy as np
def can_pass(matrix, first, second):
    global row, col
    row = len(matrix[0])
    col = len(matrix)
    vizit = np.zeros((col,row))
    return  f(first, second,vizit,matrix)

def f(first, second, vizit, matrix):
    if first == second:
        return True
    if first[0] + 1 < col and matrix[first[0] + 1][first[1]] == matrix[first[0]][first[1]] and vizit[first[0] + 1, first[1]] == 0:
        vizit[first[0] + 1, first[1]] = 1
        if f((first[0] + 1, first[1]), second,vizit,matrix): 
            return True
    if first[0] - 1 >= 0 and matrix[first[0] - 1][first[1]] == matrix[first[0]][first[1]] and vizit[first[0] - 1, first[1]] == 0:
        vizit[first[0] - 1, first[1]] = 1
        if f((first[0] - 1, first[1]), second,vizit,matrix): 
            return True
    if first[1] - 1 >= 0 and matrix[first[0]][first[1] - 1] == matrix[first[0]][first[1]] and vizit[first[0], first[1] - 1] == 0:
        vizit[first[0], first[1] - 1] = 1
        if f((first[0], first[1] - 1), second,vizit,matrix): 
            return True
    if first[1] + 1 < row and matrix[first[0]][first[1] + 1] == matrix[first[0]][first[1]] and vizit[first[0], first[1] + 1] == 0:
        vizit[first[0], first[1] + 1] = 1
        if f((first[0], first[1] + 1), second,vizit,matrix): 
            return True
    return  False

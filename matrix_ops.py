#############################################################################
# Unit for operations with matrix for calculate correlations personal koef  #
#                                                                           #    
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#############################################################################
import copy

#determinant of square matrix(any size)
def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
 
def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp
 
def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det2(matrix)
 
    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))

def get_minor(matrix,idx_row,idx_col):
    copy_matrix = copy.deepcopy(matrix)
    _ = copy_matrix.pop(idx_row)
    rows = len(copy_matrix)
    for i in range(rows):
        _ = copy_matrix[i].pop(idx_col)
    return copy_matrix


# m = [[2.0,4,1,1],
#      [0.1,2,1,0],
#      [2,1.5,1,3],
#      [-4,0,0.2,3]]
 
# print(determinant_(m))
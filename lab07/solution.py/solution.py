import  numpy as np

def reshape_rows(values, width):
    val_len = len(values)
    if (val_len % width)!= 0: return []
    values = np.array(values, dtype=float)
    return values.reshape(val_len//width, width).tolist()

def block(matrix, rows, columns):
    new_mat = np.array(matrix, dtype=float)
    r1, r2 = rows[0], rows[1]
    c1, c2 = columns[0], columns[1] + 1
    return new_mat[[r1,r2], c1:c2].tolist()

def column_means(matrix):
    matrix = np.array(matrix, dtype=float)
    return np.round(matrix.mean(axis=0), 1).tolist()

def column_range(matrix, column):
    matrix = np.array(matrix, dtype=float)
    mmax = matrix[:, column].max() - matrix[:, column].min()
    return round(mmax, 6)

print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))
# [[12.0, 14.5, 11.0], [13.0, 15.5, 10.5]]

print(block([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 2], [1, 2]))
# # [[2.0, 3.0], [8.0, 9.0]]

print(column_means([[1, 2], [3, 4], [5, 6]]))
# [3.0, 4.0]

print(column_range([[1, 2], [5, 7]], 1))         
# 5.0
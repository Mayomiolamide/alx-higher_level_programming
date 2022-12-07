def sqaure_matrix_simple(matrix=[]):
    tmp = []
    for x in matrix:
        tmp.append(list(map(lamda x: x**2, x)))
    return (tmp)

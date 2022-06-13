def transpose(matrix):
    col = len(matrix[0])
    array = matrix.copy()
    matrix.clear()
    for i in range(col):
        for_set = []
        for j in range(len(array)):
            for_set.append(array[j][i])
        matrix.append(for_set)

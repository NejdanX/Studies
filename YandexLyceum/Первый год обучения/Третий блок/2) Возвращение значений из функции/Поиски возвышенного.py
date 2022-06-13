def find_mountain(heightsMap):
    maximum_height = 0
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if maximum_height < heightsMap[i][j]:
                maximum_height = heightsMap[i][j]
                row, col = i, j
    return row, col

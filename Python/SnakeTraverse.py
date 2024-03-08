def spiralTraverse(array):
    rowIndex = 0
    colIndex = 0
    newArray = []
    while rowIndex < len(array):
        if rowIndex % 2 == 0:
            if colIndex < len(array[rowIndex]):
                newArray.append(array[rowIndex][colIndex])
                colIndex += 1
            else:
                colIndex = -1
                rowIndex += 1
        else:
            if colIndex >= 0 - len(array[rowIndex]):
                newArray.append(array[rowIndex][colIndex])
                colIndex -= 1
            else:
                colIndex = 0
                rowIndex += 1
    return newArray

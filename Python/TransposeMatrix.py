# LINK: https://www.algoexpert.io/questions/transpose-matrix
def transposeMatrix(matrix):
    tMatrix = []
    for _ in range(len(matrix[0])):
        tMatrix.append([])

    for row in matrix:
        for index, element in enumerate(row):
            tMatrix[index].append(element)
    # Write your code here.
    return tMatrix

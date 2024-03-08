# LINK: https://www.algoexpert.io/questions/spiral-traverse
def spiralTraverse(array):
    numRows = len(array)
    numCols = len(array[0])

    startRow = 0
    startCol = 0
    # Write your code here.
    rowIndex = 0
    colIndex = 0

    newArray = []

    # 0 -> right
    # 1 -> down
    # 2 -> left
    # 3 -> up
    dir = 0

    while len(newArray) < (len(array) * len(array[0])):
        if rowIndex < len(array) and colIndex < len(array[0]):
            newArray.append(array[rowIndex][colIndex])

        if dir % 4 == 0:
            if colIndex < numCols - 1:
                colIndex += 1
            else:
                numCols -= 1
                rowIndex += 1
                dir += 1
        # Go Down
        elif dir % 4 == 1:
            if rowIndex < numRows - 1:
                rowIndex += 1
            else:
                numRows -= 1
                colIndex -= 1
                dir += 1

        # Go Left
        elif dir % 4 == 2:
            if colIndex > startCol:
                colIndex -= 1
            else:
                startCol += 1
                rowIndex -= 1
                dir += 1

        # Go Up
        else:
            if rowIndex > startRow + 1:
                rowIndex -= 1
            else:
                startRow += 1
                colIndex += 1
                dir += 1

    return newArray

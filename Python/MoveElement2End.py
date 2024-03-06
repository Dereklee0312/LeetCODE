def moveElementToEnd(array, toMove):
    iterations = 0
    index = 0

    while iterations < 2 * len(array):
        if array[index % len(array)] == toMove:
            array.pop(index)
            array.append(toMove)
        else:
            index += 1

        iterations += 1

    return array

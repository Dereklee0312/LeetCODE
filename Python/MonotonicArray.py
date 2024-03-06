# array= [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
array= [1,2, 2, 1]
def isMonotonic(array):
    p1 = 0
    p2 = 1
    trend = ""
    while p2 < len(array):
        if trend == "":
            if array[p2] > array[p1]:
                trend = "UP"
            elif array[p2] < array[p1]:
                trend = "DOWN"
        elif trend == "UP":
            if array[p2] < array[p1]:
                return False
        elif trend == "DOWN":
            if array[p2] > array[p1]:
                return False
        p1 += 1
        p2 += 1

    return True

print(isMonotonic(array))

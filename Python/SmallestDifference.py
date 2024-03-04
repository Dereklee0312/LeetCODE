def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    p1, p2 = 0, 0

    closestDist = abs(arrayOne[p1] - arrayTwo[p2])
    curClosest = [arrayOne[p1], arrayTwo[p2]]

    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        distance = arrayOne[p1] - arrayTwo[p2]
        print(closestDist, distance, " | ", arrayOne[p1], arrayTwo[p2])
        if abs(distance) < closestDist:
            curClosest = [arrayOne[p1], arrayTwo[p2]]
            closestDist = abs(distance)

        if distance < 0:
            p1 += 1
        elif distance > 0:
            p2 += 1
        else:
            return [arrayOne[p1], arrayTwo[p2]]

    return curClosest

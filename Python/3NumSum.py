# array= [1, 2, 3]
# targetSum= 6
array= [12, 3, 1, 2, -6, 5, 0, -8,-1, 6, -5]
targetSum= 0
# array= [1, 2, 3]
# targetSum= 7

def threeNumberSum(array, targetSum):
    numArray = []
    array.sort()
    for index1, num1 in enumerate(array):
        targetNum1 = targetSum - num1
        array.remove(num1)
        for index2, num2 in enumerate(array):
            targetNum2 = targetNum1 - num2
            array.remove(num2)
            if targetNum2 in array and [num1, num2, targetNum2] not in numArray:
                numArray.append([num1, num2, targetNum2])
            array.insert(index2, num2)
        array.insert(index1, num1)
        
    return sorted(numArray)

print(threeNumberSum(array, targetSum))
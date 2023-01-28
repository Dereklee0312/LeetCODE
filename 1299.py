# Author: Derek Lee
# Start Date: 27-01-2023
# End Date: 27-01-2023
# Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# Difficulty: Easy
#
#
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
#
#
#
# Example 1:
#
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation:
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:
#
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
#
#
# Constraints:
#
# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        Solution 1:
        Runtime: 804 ms
        Mem Usage: 15.6 MB

        - If arr contains only one element, automatically swapped with -1 as no element on the right
        - With more than one element, find the max to the right of first element
        - Enter loop and start swapping current number with max, until max number is reached within the iteration
            - Find new max, then swap again
        - When reaching last element, automatically swap with -1

        NOTE:
            Simply finding the max value to the right for each iteration is possible but would exceed runtime constraints
        '''
        if len(arr) == 1:
            return [-1]

        curMax = max(arr[1:])

        for i in range(len(arr)):
            if i + 1 != len(arr):
                if arr[i] == curMax:
                    curMax = max(arr[i + 1 :])
                    arr[i] = curMax
                else:
                    arr[i] = curMax

            else:
                arr[i] = -1

        return arr

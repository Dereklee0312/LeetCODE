"""
Author: Derek Lee
Date Started: 31 Oct 2022
Date Completed:
Link: https://leetcode.com/problems/two-sum/

Qu 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""


class Solution:
    """
    Solution 1:
    Runtime: 8395 ms
    Mem Usage: 14.8 MB

    Way too slow because using nested loops and nested conditions.

    - For each number in the list, go through the list again until the addition of the numbers = target
      but the second number should not be at same index as first number
    - Goes through each number through the nested loop.
    - First condition ensures that the indexes do not correspond.
    - Second condition returns the list of indexes if correct combination is found.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            firstNum = nums[i]
            for j in range(len(nums)):
                if j != i:
                    secondNum = nums[j]
                    if firstNum + secondNum == target:
                        return [i, j]

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Solution 2:
        Runtime: 1617 ms
        Mem Use: 14.9 MB

        Still uses a loop, but more efficient since only one loop and condition is used.

        Reverse logic is used:
        - For each number in list, find the remainder when substracting from target
        - Condition checks if the remainder is in the list and check if index of remainder is not same as first number
        - Return list of the indexes if conditions are satisfied
        """
        for h, i in enumerate(nums):
            remainder = target - i
            if (remainder in nums) and (nums.index(remainder) != h):
                return [h, nums.index(remainder)]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        Solution 3:
        Runtime: 124 ms
        Mem Use: 15.2 MB

        Still uses a loop, but uses a dictionary instead of the list method, index

        Reason why dictionary is much faster than list is because dictionary uses hash tables and the average lookup time
        is O(1) whereas a list is iterative.
        Source: https://stackoverflow.com/questions/38927794/python-dictionary-vs-list-which-is-faster

        Explanation of solution:
        - Uses almost same logic as sol 2
        - Iterate through list of numbers with enumerate to get index simultaneously
        - Find remainder 
        - Check if remainder is in dictionary
            -> True, Return list of indexes 
            -> False, Add new value & index to dictionary

        NOTE: Only add the new value to dictionary if the remainder is not in the dictionary to bypass checking if index is repeating
              That is, for each new iteration, if the remainder for the current iteration is in the dictionary, there is no way
              that it would be the same index as the current iteration as it has not been added yet.

              Reason why the value is used as key instead of index is to retrieve the index based on the value.
        """

        dict = {}

        for index, value in enumerate(nums):
            remainder = target - value

            if (remainder in dict):
                return [index, dict[remainder]]

            dict[value] = index

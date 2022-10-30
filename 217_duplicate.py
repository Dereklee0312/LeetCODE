"""
Author: Derek Lee
Date Started: ???
Date Completed: ?? (1st attempt)
                30 Oct 2022 (2nd attempt)
Link: https://leetcode.com/problems/contains-duplicate/

Qu 217. Contains duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    """
    Solution 1:

    Ans:
    1) Sorted the list such that any duplicates will be next to each other
    2) Used an enum for loop to get 2 values for comparison
    3) As soon as a duplicate happens return True, otherwise return False
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i, j in enumerate(nums):
            if i < len(nums) - 1 and j == nums[i + 1]:
                return True

        return False

    """
    Solution 2:
    Runtime = 455 ms
    Mem Usage = 26.1 MB

    - Since sets remove any duplicateds, simply convert the list into a set and check if length is the same
    - Use != since method should:
        return True when there are duplicates 
        return False when everything is distinct
    """

    def containsDuplicate1(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

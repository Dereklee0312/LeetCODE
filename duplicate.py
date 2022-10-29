class Solution:
    """
    Qu:
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

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

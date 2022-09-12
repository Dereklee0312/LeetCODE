class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i,j in enumerate(nums):
            if i < len(nums)-1 and j == nums[i+1]:
                return True

        return False

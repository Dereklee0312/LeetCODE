# Author: Derek Lee
# Start Date: 29-01-2023
# End Date: 29-01-2023
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium
#
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution:
    """
    TIPS FROM Submissions:
        1 - HEAP DS
        2 - Counter from collections
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Solution 1:
        Runtime: 1713 ms
        Mem Usage: 18.7 MB

        - Very inefficient process
        1 - Dictionary ~ Number : Count of num
        2 - Sort dictionary
        3 - Iterate k time and append to list
        """
        # Dictionary
        # num: count of number
        maps = {}
        for num in set(nums):
            maps[num] = nums.count(num)

        sort = sorted(maps.items(), key=lambda x: x[1], reverse=True)

        lst = []
        for _ in range(k):
            lst.append(sort[_][0])

        return lst

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        """
        Simply refactor of first solution
        """
        counts = []
        for num in set(nums):
            counts.append((num, nums.count(num)))

        return [x[0] for x in sorted(counts, key=lambda x: x[1], reverse=True)[:k]]

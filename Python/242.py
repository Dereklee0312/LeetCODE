# Author: Derek Lee
# Start Date: 27-01-2023
# End Date: 27-01-2023
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
#
# Valid Anagram
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Solution 1:
        Runtime: 77 ms
        Mem Usage: 15.7 MB

        - Simply check if s and t contain the same characters
        '''
        return sorted(list(s)) == sorted(list(t))

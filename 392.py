# Author: Derek Lee
# Start Date: 28-01-2023
# End Date: 28-01-2023
# Link: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy
#
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Solution 1:
        Runtime: 32 ms
        Mem Usage: 13.9 MB

        - Focuses on finding the index of the occurrence of the chars from `s` in `t`
        - Checks if the order is correct to ensure it is a subsequence
        - Reverse the strings to remove need to check whether the first occurrence of the character needs to be discarded
            - Ex: s = 'ab'  t = 'baab'
            - If not reversed, b's index would be 0 and thus would not be considered a substring as a's index would be 1
            - Another check would be required to ensure all occurrences of a letter is considered
        """
        indLst = []
        t = t[::-1]

        for char in s[::-1]:
            if char in t:
                indLst.append(t.index(char))
                t = t.replace(char, "", 1)

            else:
                return False

        return sorted(indLst) == indLst

    def isSubsequence1(self, s, t):
        '''
        Solution 2:
        Runtime: 31 ms
        Mem Usage: 13.8 MB

        NeetCode solution
        - Basically uses 2 pointers `L` for `s` and `R` for `t`
        - Increment L pointer only when both point to same character
        - Increment R if pointer point to same character so as to eliminate char from subsequence
        - Increment R if pointer does not point to same character to check next char
        '''
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i == len(s) else False

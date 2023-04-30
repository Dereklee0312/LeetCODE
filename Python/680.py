# Author: Derek Lee
# Start Date: 04-02-2023
# End Date:
# Link: https://leetcode.com/problems/valid-palindrome-ii/
# Difficulty: Easy
#
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
#
#
# Example 1:
#
# Input: s = "aba"
# Output: true
# Example 2:
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
#
# Input: s = "abc"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1] == s:
            return True

        cont = True

        for i in range(len(s)):
            newStr = s[0:i] + s[i + 1 :]
            if newStr[::-1] == newStr:
                return True
        return False

"""
Author: Derek Lee
Start Date: 29-12-2022
End Date:
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium

Given a string s, find the length of the longest
substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct = ""
        distLst = set()
        for char in s:
            print(char, distinct)
            if char not in distinct:
                distinct += char
            else:
                distLst.add(distinct)
                distinct = char

        return len(max(distLst, key=len)) if len(distLst) != 0 else 0

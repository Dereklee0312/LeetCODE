"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestStr = min(strs, key=len)

        common = ""
        stop = False
        for i, char in enumerate(shortestStr):
            for string in strs:
                if string[i] == char:
                    continue
                else:
                    stop = True
            else:
                if stop:
                    break
                else:
                    common += char

        return common

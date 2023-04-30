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
        '''
        Solution 1:
        Runtime: 40 ms
        Mem Usage: 14 MB

        NOTE:
            min, max functions can take an additional paramenter, key to specify which property to use when sorting

        - Find shortest string (SS) from list
        - Iterate through SS with an index anchor
            - For each iteration, Iterate through list of strings
                - Check if character at current index of each string == character of current iteration
            - If Characters do not correspond, break from loops
            - Else, add characters to common string
        '''
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

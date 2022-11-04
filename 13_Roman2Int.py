"""
Author: Derek Lee
Date Started: 1 Nov 2022
Date Completed: 1 Nov 2022
Link: https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    """
    Sol 1:
    Runtime: 45 ms
    Mem Use: 13.9 MB

    Fast but not most efficient since using 2 separate dictionaries as well as 2 loops.
    - First dictionary represents the Numerals that are exceptions
    - Second one is for regular ones
    - Create a list of all exceptions that need to be removed from the string

    - First loop removes the exceptions from the string and adds to value
    - Second loop adds to value according to remaining numerals
    """

    def romanToInt(self, s: str) -> int:
        exceptions = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        regular = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        value = 0

        toRemove = [x for x in exceptions.keys() if x in s]

        for i in toRemove:
            value += exceptions[i]
            s = s.replace(i, "")

        for j in s:
            value += regular[j]

        return value

    def romanToInt1(self, s: str) -> int:
        """
        Sol 2:
        Runtime: 107 ms
        Mem Use: 14 MB

        Very slow as it requires a lot of computation and has 3 conditions to check for each iteration
        - Create a dictionary with all the numerals and their value
        - Iterate through the string in reverse order
        - Check if the next value is less than the current value
            - If value is less, subtract to total and add index to characters to be skipped
        - Check if current index is none as a roman numeral may not contain any exceptions
        - Check if current index is not the one to be skipped
            - If not, add value to total
        """

        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        skip = None

        for index, char in enumerate(s[::-1]):
            if (romans[s[len(s) - index - 2]] < romans[char]) and (index != len(s) - 1):
                total -= romans[s[len(s) - index - 2]]
                skip = len(s) - index - 2
            if skip == None:
                total += romans[char]
            elif index != len(s) - skip - 1:
                total += romans[char]

        return total

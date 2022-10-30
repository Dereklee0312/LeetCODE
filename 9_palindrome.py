"""
Qu 9. Palindrome number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-2^31 <= x <= 2^31 - 1
"""

class Solution:
    """
    Solution 1:

    This solution is not the best but is my first attempt.
    Runtime = 195 ms
    Memory usage = 13.8 MB

    1) Convert the number to string
    2) Reverse the order of the string by starting from the end with a for loop
    3) Check if reversed string is same as initial string
    """

    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        newstr = ""
        for i in range(len(num)):
            newstr += num[len(num) - i - 1]

        if newstr == num:
            return True
        else:
            return False

    """
    Solution 2:

    Second attempt - Make it faster
    Runtime = 104 ms
    Mem Use = 14 MB

    Simply convert first solution to a 1 liner by using string indexing instead of a loop
    """

    def isPalindrome1(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    """
    Solution 3:

    Attempt to solve it without converting to string


    """

    def isPalindrome2(self, x: int) -> bool:
        if x >= 0:
            reversed = 0
            x1 = x
            while x1 != 0:
                digit = x1 % 10
                reversed = reversed * 10 + digit
                x1 //= 10

            if reversed == x:
                return True
            else:
                return False
        else:
            return False


test = Solution()
print(test.isPalindrome2(10100101))

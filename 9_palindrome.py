class Solution:
    '''
    Solution 1:

    This solution is not the best but is my first attempt.
    Runtime = 195 ms
    Memory usage = 13.8 MB

    1) Convert the number to string
    2) Reverse the order of the string by starting from the end with a for loop
    3) Check if reversed string is same as initial string
    '''
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        newstr = ""
        for i in range(len(num)):
            newstr += num[len(num)-i-1]

        if newstr == num:
            return True
        else:
            return False

    '''
    Solution 2:

    Second attempt - Try to solve it without changing to string
    '''
    def IsPalindrome(self, x: int) -> bool:

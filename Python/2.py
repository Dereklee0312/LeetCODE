"""
Author: Derek Lee
Start Date: 29-12-2022
End Date: 29-12-2022
Link: https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    Solution 2:
    Runtime: 77 ms
    Mem Usage: 13.9 MB

    - Generate the numbers with `createNum`
    - Return LinkedList with `createLinkedLst`
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.createNum(l1)
        num2 = self.createNum(l2)

        return self.createLinkedLst(num1 + num2)

    def createNum(self, lst) -> int:
        """
        lst: Head of LinkeList
        Return: reversed number (int)

        - Iterate through linked list and append each number to a string.
        - Convert reversed string to int
        """
        curVal = lst.val
        num = str(curVal)

        while lst.next != None:
            curVal = lst.next.val
            num += str(curVal)
            lst = lst.next

        return int(num[::-1])

    def createLinkedLst(self, number) -> ListNode:
        """
        number: int
        Return: Head of LinkedList

        - Reverse order of number
        - Create Head Node from first number and keep reference of Head
        - Iterate through remaining reversed numbers and sequentially link each node
        """
        number = str(number)[::-1]
        curNode = ListNode(int(number[0]))

        # Keep reference to firstNode
        firstNode = curNode

        for num in (number[1:]):
            curNode.next = ListNode(int(num))
            curNode = curNode.next

        return firstNode

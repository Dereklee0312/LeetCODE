# Author: Derek Lee
# Start Date: 30-01-2023
# End Date:
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
#
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        curNode = head
        lst = [curNode.val]

        while curNode.next != None:
            lst.append(curNode.next.val)
            curNode = curNode.next

        newList = ListNode(lst[-1])
        curNode = newList
        for i in lst[-2::-1]:
            newNode = ListNode(i)
            curNode.next = newNode
            curNode = curNode.next

        return newList

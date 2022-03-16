"""
Q206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        revList = ListNode(val=head.val, next=None)
        head = head.next
        
        while head:
            newHead = ListNode(val = head.val, next = revList)
            revList = newHead 
            head = head.next
        return revList
            
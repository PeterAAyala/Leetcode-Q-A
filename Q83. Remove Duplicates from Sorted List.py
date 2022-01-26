"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that 
each element appears only once. Return the linked list sorted as well.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if first == None:
            return head
        
        second = head.next 
        
        while second:
            if first.val == second.val:
                first.next = second.next
                second = second.next
            else:
                first = second 
                second = second.next
                
        return head 
        
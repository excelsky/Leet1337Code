# https://leetcode.com/problems/sort-list
# 6 gaksu

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge( a, b):
            
            if not a:
                return b
            
            elif not b:
                return a
            
            if a.val < b.val:
                a.next = merge(a.next, b)
                return a
                
            else:
                b.next = merge(a, b.next)
                return b
        
        
        ## base case
        
        if head is None:
            # empty node
            return None
        
        elif head.next is None:
            # one node only
            return head
        
        ## general case
        # divide into two halves
        
        pre, slow, fast = None, head, head
        
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        
        pre.next = None

        
        # sort by divide-and-conquer
        
        a = self.sortList(head)
        b = self.sortList(slow)
        result = merge(a, b)
        return result
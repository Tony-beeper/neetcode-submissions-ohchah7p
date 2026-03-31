# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 1
        start = head
        while start.next:
            start = start.next
            size += 1
        
        idx = size - n

        if idx == 0:
            return head.next

        start = head
        prev = None
        next_node = None
        while idx != 0:
            prev = start
            start = start.next
            idx -= 1
        prev.next = start.next
        return head

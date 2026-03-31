# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        prev = None
        while a != None:
            buffer1 = a.next
            buffer2 = a
            a.next = prev
            a = buffer1
            prev = buffer2
        
        return prev

            






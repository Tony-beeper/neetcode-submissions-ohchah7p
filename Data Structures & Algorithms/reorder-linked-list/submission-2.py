# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow = head
        fast = head
        prev = None
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        prev.next = None # breaking two

        prev = None
        while slow:
            buf = slow.next
            slow.next = prev
            prev = slow
            slow = buf
        l2 = prev
        l1 = head
        
        cur = None
        while l1 and l2:
            cur = l1
            buf1 = l1.next
            buf2 = l2.next 
            l1.next = l2
            l2.next = buf1
            l1 = buf1
            l2 = buf2
            # l1.next 
        if l2:
            cur.next = l2
        return









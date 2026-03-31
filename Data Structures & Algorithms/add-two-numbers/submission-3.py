# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        start = l1
        end = None
        prev_1 = None
        prev_2 = None
        while l1 != None and l2!= None:
            val = 0
            val1 = l1.val
            val2 = l2.val
            val = val1 + val2
            if carry:
                val = val + 1
                carry = False
            if val >= 10:
                carry = True
                val = val - 10
            # print(val)

            l1.val = val
            end = l1
            prev1 = l1
            prev2 = l2
            l1 = l1.next
            l2 = l2.next
        if l1 == None and l2 != None:
            prev1.next = l2
            while l2:
                val = l2.val
                if carry:
                    val = val + 1
                    carry = False
                if val >= 10:
                    carry = True
                    val = val - 10
                l2.val = val
                end = l2
                l2 = l2.next
        elif l1 != None and l2 == None:
            while l1:
                val = l1.val
                if carry:
                    val = val + 1
                    carry = False
                if val >= 10:
                    carry = True
                    val = val - 10
                l1.val = val
                end = l1
                l1 = l1.next





        # print(carry)
        if carry:
            end.next = ListNode(1)
        return start
            


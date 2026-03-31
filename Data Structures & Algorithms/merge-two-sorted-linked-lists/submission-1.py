# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 == None:
#             return list2
#         elif list2 == None:
#             return list1

#         cur_1 = list1
#         cur_2 = list2
#         cur_ptr = None
#         head = None
#         if cur_1.val > cur_2.val:
#             cur_ptr = cur_2
#             # head = cur_ptr
#             cur_2 = cur_2.next
#         else:
#             cur_ptr = cur_1
            
#             cur_1 = cur_1.next
#         head = cur_ptr

#         while cur_1 != None or cur_2 != None:
#             if cur_1 != None and cur_2 != None:
#                 if cur_1.val >= cur_2.val:
#                     buf = cur_2.next
#                     cur_ptr.next = cur_2
#                     cur_ptr = cur_2
#                     cur_2 = buf
#                 else:
#                     buf = cur_1.next
#                     cur_ptr.next = cur_1
#                     cur_ptr = cur_1
#                     cur_1 = buf
#             elif cur_1 == None:
#                 cur_ptr.next = cur_2
#                 break
#             else:
#                 cur_ptr.next = cur_1
#                 break
#         return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next
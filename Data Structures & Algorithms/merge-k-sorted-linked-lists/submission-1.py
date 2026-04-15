# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1 or not lists[0]:
            return None
        def merge_two(a,b):
            if a == None or b == None:
                
                return a if not b else b
            dummy = ListNode(0)
            cur = dummy

            while a and b:
                if a.val > b.val:
                    cur.next = b
                    b = b.next
                else:
                    cur.next = a
                    a = a.next
                cur = cur.next
            cur.next = a if a else b
            return dummy.next

        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i+1] if i + 1 < len(lists) else None
                element = merge_two(a,b)
                new_list.append(element)
            lists = new_list
        
        return lists[0]

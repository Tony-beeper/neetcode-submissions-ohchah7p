class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            lst = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i + 1] if i < len(lists)-1 else None
                new = self.merge_two(a,b)
                lst.append(new)
            lists = lst
            # print(lists)
        return lists[0]

    def merge_two(self, a, b):
        if not a or not b:
            return a if a else b
        # print("hi")
        dummy = ListNode(0)
        cur = dummy

        while a and b:
            if a.val >= b.val:
                cur.next = b
                b = b.next
            else:
                cur.next = a
                a = a.next
            cur = cur.next
        cur.next = a or b
        return dummy.next











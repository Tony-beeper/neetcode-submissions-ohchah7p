"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # print(head)
        arr = []
        counter = 0
        start = head
        # while head != None:
        #     arr.append((head.val,head.next,head.random, False, counter))
        #     head = head.next
        #     counter += 1
        dummy = Node(0)
        prev = dummy
        hash_set = {}
        while start:
            cur = Node(start.val)
            cur.next = start.next
            prev.next = cur
            hash_set[start] = cur
            start = start.next
            prev = cur
        start = head
        while start:
            cur = hash_set[start]
            
            cur.random = hash_set[start.random] if start.random else None
            start = start.next
        return dummy.next





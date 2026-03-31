# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return
        start = head
        end = head
        counter = 1
        while end.next != None:
            end = end.next
            counter += 1

        splitting_point = counter // 2
        # print(str(splitting_point))
        head_of_split = head
        while splitting_point != 0:
            buf = head_of_split.next
            if splitting_point == 1:
                head_of_split.next = None
            head_of_split = buf
            splitting_point -= 1
        
        # reverse starting the splittingpoint
        # print("debug")
        prev = None
        while head_of_split != None:
            
            buf = head_of_split.next
            head_of_split.next = prev
            prev = head_of_split
            head_of_split = buf
        head_of_split = prev

        # print("debug2")
        # odd = True
        
        while head_of_split != None:
            print(str(head_of_split.val))
            buf2 = head_of_split.next
            buf = start.next
            if buf == None:
                start.next = head_of_split
                break
            start.next = head_of_split
            start.next.next = buf
            head_of_split = buf2
            start = buf

        return None

            


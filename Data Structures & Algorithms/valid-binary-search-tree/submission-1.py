# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        small = -float('inf')
        big = float('inf')
        def bfs(node, smallest, biggest):
            if not node:
                return True
            
            if node.val <= smallest:
                print("hi")
                return False
            if node.val >= biggest:
                print("hi")
                return False
            new_smallest = max(smallest, node.val)
            new_biggest = min(biggest,node.val)
            
            return bfs(node.left,smallest,new_biggest) and bfs(node.right,new_smallest,biggest)
        return bfs(root,small,big)
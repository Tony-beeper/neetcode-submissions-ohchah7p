# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same =True
        def bfs(p,q):
            nonlocal same
            
            if p == None and q == None:
                return
            elif p == None or q == None:
                same = False
                return
            if p.val != q.val:
                same = False
                return
            bfs(p.left,q.left)
            bfs(p.right,q.right)
        bfs(p,q)

        return same
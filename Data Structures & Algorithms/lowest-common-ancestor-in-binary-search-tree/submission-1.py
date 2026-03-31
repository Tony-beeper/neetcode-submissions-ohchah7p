# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def bfs(a):
            if not a:
                return None
            if (p.val <= a.val and a.val <= q.val) or (q.val <= a.val and a.val <= p.val):
                return a
            if a.val >= p.val and a.val >= q.val:
                return bfs(a.left)
            if a.val <= p.val and a.val <= q.val:
                return bfs(a.right)
        return bfs(root)

            
            
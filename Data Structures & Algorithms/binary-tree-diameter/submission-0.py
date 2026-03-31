# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        def dfs(node):
            nonlocal diam
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diam = max(diam, left+right)
            # print(left)
            return max(left,right) + 1
        dfs(root)
        return diam
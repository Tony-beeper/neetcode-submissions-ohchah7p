# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        counter = 0
        def bfs(node,greatest):
            nonlocal counter
            if node == None:
                return
            if node.val >= greatest:
                counter += 1
                greatest = node.val
            bfs(node.left, greatest)
            bfs(node.right, greatest)
            



        bfs(root, root.val)

        return counter
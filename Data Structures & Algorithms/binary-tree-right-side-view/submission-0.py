# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_hash = {}
        arr = []
        def bfs(node,level):
            if not node:
                return
            if not level_hash.get(level,False):
                level_hash[level] = True
                arr.append(node.val)
            level += 1
            bfs(node.right, level)
            bfs(node.left, level)
        bfs(root,0)
        return arr


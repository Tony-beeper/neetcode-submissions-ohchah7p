# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        arr = []

        def bfs(node, level):
            # if node == None:
                # return

            if len(arr) <= level:
                arr.append([])

            arr[level].append(node.val)
            
            level+=1
            if node.left != None:
                bfs(node.left, level)
            if node.right != None:
                bfs(node.right, level)

        bfs(root,0)

        return arr
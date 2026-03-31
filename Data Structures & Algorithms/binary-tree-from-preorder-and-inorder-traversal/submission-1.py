# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def buildT(preord, inord):
            if len(preord) == 0:
                return None
            root_val = preord[0]
            root = TreeNode(root_val)

            mid = inord.index(root_val)

            root.left = buildT(preord[1:1+mid],inord[:mid])
            root.right = buildT(preord[1+mid:],inord[mid+1:])

            return root
        
        return buildT(preorder, inorder)
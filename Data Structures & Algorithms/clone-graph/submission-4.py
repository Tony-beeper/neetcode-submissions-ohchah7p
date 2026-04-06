"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return
        old_to_new = {}

        def dfs(node):
            if old_to_new.get(node)!= None:
                return old_to_new[node]
            # print("hi")

            cur_node = Node(node.val)
            old_to_new[node] = cur_node
            # cur_node.
            for neighbor in node.neighbors:
                cur_node.neighbors.append(dfs(neighbor))
            return cur_node
        return dfs(node)



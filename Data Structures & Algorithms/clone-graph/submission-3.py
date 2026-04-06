"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFSBFSBFS
        if not node:
            return
        neighbors = {}
        old_node = node
        lst = [node]
        counter = 0
        head = None
        while lst:
            node = lst.pop(0)
            new_node = Node(node.val)
            new_node.neighbors = []
            if counter == 0:
                head = new_node
            neighbors[node.val] = new_node
            counter += 1
            for neighbor in node.neighbors:
                if neighbors.get(neighbor.val) == None:
                    lst.append(neighbor)
        lst = [old_node]
        visited = [False for _ in range(counter+1)]

        while lst:
            node = lst.pop(0)
            cur_node = neighbors[node.val]
            visited[node.val] = True
            for neighbor in node.neighbors:
                cur_node.neighbors.append(neighbors[neighbor.val])
                if visited[neighbor.val] == False:
                    lst.append(neighbor)
                    visited[neighbor.val] = True
        
        return head
                
            
            



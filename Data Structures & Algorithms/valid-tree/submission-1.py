class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes_passed = 0
        passed_by = set()
        neighbors = defaultdict(list)
        for a,b in edges:
            neighbors[b].append(a)
            neighbors[a].append(b)
        # print(neighbors)
        def dfs(node, parent, nodes_passed):
            passed_by.add(node)
            nodes_passed += 1

            for neighbor in neighbors[node]:
                if neighbor in passed_by and neighbor != parent:
                    return False
                if neighbor == parent:
                    continue
                else:
                    dfs(neighbor, node, nodes_passed)
            return True
        
        if dfs(0, None, nodes_passed) and len(passed_by) == n:
            return True
        # print(passed_by)
        return False
            







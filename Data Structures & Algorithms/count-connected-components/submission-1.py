class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        nodes = set()
        counter = 0
        for edge in edges:
            a = edge[0]
            b = edge[1]
            graph[a].add(b)
            graph[b].add(a)
            nodes.add(a)
            nodes.add(b)

        visited = {}
        for node in nodes:
            visited[node] = False

        def dfs(node):
            if visited[node]:
                return False
            visited[node] = True
            for element in graph[node]:
                dfs(element)
            return True



        for node in nodes:
            if dfs(node):
                counter += 1
        return (n - len(nodes)) + counter
        # return 
        
            
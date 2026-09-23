class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n-1:
            return False

        if not n:
            return True

        adj = {i : [] for i in range(n)} 
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        visited = set()
        def dfs(node, prev_node):
            if node in visited:
                return False

            visited.add(node)

            for neighbour in adj[node]:
                if neighbour == prev_node:
                    continue

                if not dfs(neighbour, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
                
     


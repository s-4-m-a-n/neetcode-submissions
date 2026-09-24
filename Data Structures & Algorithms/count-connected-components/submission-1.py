class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        hashMap = {i:[] for i in range(n)}

        for a, b in edges:
            hashMap[a].append(b)
            hashMap[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbour in hashMap[node]:
                if not neighbour in visited:
                    dfs(neighbour)
                    
        counts = 0
        for node in hashMap.keys():
            if not node in visited:
                dfs(node)
                counts += 1
        return counts
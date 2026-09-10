class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n_rows, n_cols = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    next_r, next_c = row + dr, col + dc
                    if (next_r in range(n_rows) and 
                       next_c in range(n_cols) and
                       grid[next_r][next_c] == "1" and
                       (next_r, next_c) not in visited):

                       q.append((next_r, next_c))
                       visited.add((next_r, next_c))

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island += 1 
        return island
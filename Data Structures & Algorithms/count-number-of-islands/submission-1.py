class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None

        n_rows, n_cols = len(grid), len(grid[0])
        visited = set()
        num_of_island = 0

        def dfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                curr_r, curr_c = queue.popleft()
                directions = [[1, 0], [-1, 0],
                              [0, 1], [0, -1]]
                for dr, dc in directions:
                    next_r = curr_r + dr
                    next_c = curr_c + dc

                    if ((next_r, next_c) not in visited and
                       next_r in range(n_rows) and 
                       next_c in range(n_cols) and 
                       grid[next_r][next_c] == "1"):

                       queue.append((next_r, next_c))
                       visited.add((next_r, next_c))

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    num_of_island +=1
            
        return num_of_island
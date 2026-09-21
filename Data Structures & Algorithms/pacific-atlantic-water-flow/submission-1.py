class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return None
        
        n_rows, n_cols = len(heights), len(heights[0])
        paci_visited = set()
        atl_visited = set()

        def dfs(r, c, visit, prev_height):
            if ((r, c) in visit or 
                r < 0 or c < 0 or 
                r >= n_rows or c >= n_cols or
                heights[r][c] < prev_height):
                return None

            visit.add((r, c))

            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r+dr, c+dc, visit, heights[r][c])
        
        for c in range(n_cols):
            dfs(0, c, paci_visited, heights[0][c])
            dfs(n_rows-1, c, atl_visited, heights[n_rows-1][c])
        
        for r in range(n_rows):
            dfs(r, 0, paci_visited, heights[r][0])
            dfs(r, n_cols-1, atl_visited, heights[r][n_cols-1])
        
        result = []
        for r in range(n_rows):
            for c in range(n_cols):
                if ((r, c) in paci_visited and 
                    (r, c) in atl_visited):
                    result.append([r, c])
        return result

            

         


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows, n_cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
                r >= n_rows or c >= n_cols or
                word[i] != board[r][c] or 
                (r,c) in visited):
                return False
            
            visited.add((r, c))

            res = (dfs(r+1, c, i+1) or 
                   dfs(r-1, c, i+1) or 
                   dfs(r, c+1, i+1) or 
                   dfs(r, c-1, i+1))
            
            visited.remove((r, c))

            return res

        for r in range(n_rows):
            for c in range(n_cols):
                res = dfs(r, c, 0)
                if res == True:
                    return True
        return False
        
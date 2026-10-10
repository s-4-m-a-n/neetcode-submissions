class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_rows, n_cols = len(matrix), len(matrix[0])
        row_flags = [False]*n_rows
        col_flags = [False]*n_cols
        
        # search for zeros
        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    row_flags[r] = True
                    col_flags[c] = True

        # Make rows zeros
        for r in range(n_rows):
            if row_flags[r]:
                for c in range(n_cols):
                    matrix[r][c] = 0
        
        # make cols zeros
        for c in range(n_cols):
            if col_flags[c]:
                for r in range(n_rows):
                    matrix[r][c] = 0
        
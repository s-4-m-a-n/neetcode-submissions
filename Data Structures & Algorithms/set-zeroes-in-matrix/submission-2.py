class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_rows, n_cols = len(matrix), len(matrix[0])
        
        # scan zeros and mark  rows and cols
        corner_flag = False
        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r == 0:
                        corner_flag = True
                    else:
                        matrix[r][0] = 0

        for r in range(1, n_rows):
            for c in range(1, n_cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # first column
        if matrix[0][0] == 0:
            for r in range(1, n_rows):
                matrix[r][0] = 0

        # first row
        if corner_flag:
            for c in range(n_cols):
                matrix[0][c] = 0
        

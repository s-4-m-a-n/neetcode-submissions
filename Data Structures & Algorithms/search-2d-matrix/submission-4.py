class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        l = 0
        r = (n_rows * n_cols) - 1

        while l <= r:
            p = (l + r) // 2
            # convert to 2d index
            p_r = p // n_cols
            p_c = p % n_cols

            if target == matrix[p_r][p_c]:
                return True
            elif target < matrix[p_r][p_c]:
                r = p - 1
            else:
                l = p + 1

        return False

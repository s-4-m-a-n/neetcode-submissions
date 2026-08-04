def get_2d(idx, n_cols):
    r = idx // n_cols
    c = idx % n_cols
    return r, c

def get_1d(r, c , n_cols):
    return r * n_cols + c


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])

        l = 0
        r = get_1d(n_rows-1, n_cols - 1, n_cols)

        while l <= r:
            p = (r + l)//2
            p_r, p_c = get_2d(p, n_cols)

            if matrix[p_r][p_c] == target:
                return True

            elif matrix[p_r][p_c] > target:
                r = p - 1
            else:
                l = p + 1
    
        return False

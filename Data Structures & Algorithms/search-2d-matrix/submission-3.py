class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_i, col_j = 0, len(matrix[0]) - 1
        row_i, row_j = 0, len(matrix) - 1

        while row_i <= row_j:
            current_row = (row_j + row_i) // 2
            if target < matrix[current_row][col_i]:
                row_j = current_row - 1
            elif target > matrix[current_row][col_j]:
                row_i = current_row + 1
            elif target >= matrix[current_row][col_i] and target <= matrix[current_row][col_j]:
                break # row found
            else:
                return False
            
        # search row
        while col_i <= col_j:
            p = (col_j + col_i) // 2
            if target == matrix[current_row][p]:
                return True
            elif target > matrix[current_row][p]:
                col_i = p + 1
            elif target < matrix[current_row][p]:
                col_j = p - 1
        return False

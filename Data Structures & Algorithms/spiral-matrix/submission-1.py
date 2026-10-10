class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        results = []
        
        while left <= right and top <= bottom:
            # 1. Traverse Right across the top row
            for col in range(left, right + 1):
                results.append(matrix[top][col])
            top += 1  # Shrink top boundary
            
            # 2. Traverse Down across the right column
            for row in range(top, bottom + 1):
                results.append(matrix[row][right])
            right -= 1  # Shrink right boundary
            
            # 3. Traverse Left across the bottom row (if rows remain)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    results.append(matrix[bottom][col])
                bottom -= 1  # Shrink bottom boundary
            
            # 4. Traverse Up across the left column (if columns remain)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    results.append(matrix[row][left])
                left += 1  # Shrink left boundary
                
        return results
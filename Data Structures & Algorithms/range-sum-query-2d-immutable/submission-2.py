class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, c = len(matrix), len(matrix[0])
        self.prefix_sum = [[0]*(c+1) for _ in range(n+1)]

        for i in range(n):
            prefix = 0
            for j in range(c):
                prefix += matrix[i][j]
                self.prefix_sum[i+1][j+1] = prefix + self.prefix_sum[i][j+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total = self.prefix_sum[row2+1][col2+1]
        top_residue = self.prefix_sum[row1][col2+1]
        left_residue = self.prefix_sum[row2+1][col1] 
        extra  = self.prefix_sum[row1][col1]

        return total - top_residue - left_residue + extra

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
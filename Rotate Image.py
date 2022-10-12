class Solution(object):
    def rotate(self, matrix):
        # transpose of matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        # reverse row
        for i in range(len(matrix)):
            matrix[i].reverse()

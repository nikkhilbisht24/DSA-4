class Solution(object):
    def generate(self, numRows):
        triangle = [[1]]

        for i in range(1, numRows):
            prev = triangle[i-1]
            curr = []
            curr.append(1)
            for j in range(1, i):
                curr.append(prev[j-1] + prev[j])
            curr.append(1)
            triangle.append(curr)
            
        return triangle

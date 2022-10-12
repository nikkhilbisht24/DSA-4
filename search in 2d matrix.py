class Solution(object):
    def searchMatrix(self, matrix, target):
        # TC - O(logn) + O(logm)
        
        # find out the row
        rows, cols = len(matrix), len(matrix[0])
        
        top, bottom = 0, rows-1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            
            elif target < matrix[row][0]:
                bottom = row - 1
            
            else:
                break
        
        # search the element
        row = (top+bottom)//2
        l, r = 0, cols-1
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        
        return False

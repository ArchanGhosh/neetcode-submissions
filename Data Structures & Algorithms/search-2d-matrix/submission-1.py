class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        p_row = -1
        
        for row in range(rows):
            if target<=matrix[row][-1] and target>=matrix[row][0]:
                p_row = row
                break
        if p_row == -1:
            return False    
        left, right = 0, cols-1
        
        while left<=right:
            mid = (left+right)//2
            if matrix[p_row][mid] == target:
                return True
            elif matrix[p_row][mid] < target:
                left = mid+1
            elif matrix[p_row][mid] > target:
                right = mid-1
                
        return False


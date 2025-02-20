from typing import List

## 时间：O(log m*n)   ，空间：O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                return True
        
        return False
            
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
solution = Solution()
res = solution.searchMatrix(matrix, target)
print(res) 





        
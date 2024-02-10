class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y_1, y_2 = 0, len(matrix) - 1
        while y_1 <= y_2:
            y_m = (y_2 + y_1) // 2
            if matrix[y_m][0] > target: y_2 = y_m - 1
            elif matrix[y_m][-1] < target: y_1 = y_m + 1
            else: break
        
        x_1, x_2 = 0, len(matrix[y_m]) - 1
        while x_1 <= x_2:
            x_m = (x_1 + x_2) // 2
            if matrix[y_m][x_m] > target: x_2 = x_m - 1
            elif matrix[y_m][x_m] < target: x_1 = x_m + 1
            else: return True
        
        return False

# Time complexity: O(log(M*N)) because we perform binary search to find the row which is O(log(M)) and then binary search within the row which is O(log(N)).
# Using log addditive rule log(M) + log(N) = log(M*N)

# Space complexity: O(1) because we don't need to use any extra memory other than constant values.

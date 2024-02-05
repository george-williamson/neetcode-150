class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_n: int, closed_n: int, path: str):
            if open_n == closed_n == n:
                res.append(path)
                return

            if open_n < n:
                backtrack(open_n + 1, closed_n, path+"(")
            
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path+")")

        backtrack(0, 0, "")
        return res


# Time complexity: O(4^n / (n * sqrt(n))) - related to backtracking mechanics.
# Space complexity: O(n) - we need to store 2*n in path for each valid sequence.

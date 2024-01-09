class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subgrids = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in subgrids[(r//3, c//3)]
                ): return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    subgrids[(r//3, c//3)].add(board[r][c])
        return True

#Time complexity: O(1)
#Space completxity O(1)
#Both constant due to the board being fixed 9x9

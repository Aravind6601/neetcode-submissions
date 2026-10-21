class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sq = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box = (r // 3, c //3)
                if val in rows[r] or val in cols[c] or val in sq[box]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                sq[box].add(val)
        return True
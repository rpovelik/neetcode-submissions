from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sq = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                elem = board[i][j]
                if elem == ".":
                    continue
                if elem in rows[i] or elem in cols[j] or elem in sq[i // 3 * 3 + j // 3]:
                    return False
                rows[i].add(elem)
                cols[j].add(elem)
                sq[i // 3 * 3 + j // 3].add(elem)
        
        return True
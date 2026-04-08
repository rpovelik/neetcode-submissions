class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digs = set()

        def rows(row):
            amount = 0
            for el in row:
                if el != '.':
                    digs.add(el)
                    amount += 1
            res = len(digs) == amount
            digs.clear()
            return res
        
        def cols(j):
            amount = 0
            for i in range(len(board)):
                el = board[i][j]
                if el != '.':
                    digs.add(el)
                    amount += 1
            res = len(digs) == amount
            digs.clear()
            return res
        
        def squares(r, c):
            amount = 0
            if r == 0 and c == 3:
                print(f"{r}, {c}")
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    el = board[i][j]
                    if el != ".":
                        digs.add(el)
                        amount += 1
            res = len(digs) == amount
            digs.clear()
            return res
        
        for r in board:
            if not rows(r):
                return False
        
        for c_idx in range(len(board[0])):
            if not cols(c_idx):
                return False
        
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                if not squares(i, j):
                    return False
        
        return True

[
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]
]
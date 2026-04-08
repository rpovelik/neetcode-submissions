class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_map<int, std::unordered_set<char>> rows, cols, squares;

        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[i].size(); ++j) {
                const char& cell = board[i][j];

                if (cell == '.')
                    continue;
                
                int square_idx = (i / 3) * 3 + j / 3;

                if (rows[i].count(cell) || cols[j].count(cell) || squares[square_idx].count(cell))
                    return false;
                
                rows[i].insert(cell);
                cols[j].insert(cell);
                squares[square_idx].insert(cell);
            }
        }
        return true;
    }
};

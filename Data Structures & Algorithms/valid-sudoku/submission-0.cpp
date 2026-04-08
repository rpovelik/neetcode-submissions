class Solution {
    static constexpr std::size_t board_size = 9;
    std::array<bool, board_size> checker = {false};
    
    bool check_symbol(const char& symbol) {
        if (symbol == '.')
            return true;

        if (checker.at(symbol - '1') == true)
            return false;

        checker.at(symbol - '1') = true;

        return true;
    }

    bool check_row(const std::vector<char>& row) {
        checker.fill(false);

        for (const char& symbol : row)
            if (!check_symbol(symbol))
                return false;
    
        return true;
    }

    bool check_col(const std::vector<std::vector<char>>& board, int col_idx) {
        checker.fill(false);

        for (int i = 0; i < board_size; ++i)
            if (!check_symbol(board.at(i).at(col_idx)))
                return false;
    
        return true;
    }

    
    bool check_square(const std::vector<std::vector<char>>& board, const int col_idx, const int row_idx) {
        checker.fill(false);

        for (int i = row_idx; i < row_idx + 3; ++i)
            for (int j = col_idx; j < col_idx + 3; ++j)
                if (!check_symbol(board.at(i).at(j))) {
                    return false;
                }

        return true;
    }

public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (auto& row : board)
            if (!check_row(row))
                return false;
        
        for (int col_idx = 0; col_idx < 9; ++col_idx)
            if (!check_col(board, col_idx))
                return false;
        
        for (int col_idx = 0; col_idx < 9; col_idx += 3)
            for (int row_idx = 0; row_idx < 9; row_idx += 3)
                if (!check_square(board, col_idx, row_idx))
                    return false;
        
        return true;
    }
};

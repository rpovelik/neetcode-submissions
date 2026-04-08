#include <array>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;

        std::array<int, 26> dict {0};

        for (std::size_t i = 0; i < s.size(); ++i) {
            ++dict[s[i] - 'a'];
            --dict[t[i] - 'a'];
        }

        for (auto freq : dict)
            if (freq != 0)
                return false;

        return true;
    }
};

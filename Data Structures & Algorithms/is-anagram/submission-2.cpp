class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
        
        std::array<int, 26> dict = {0};

        for (std::size_t idx = 0; idx < s.size(); ++idx) {
            ++dict[s[idx] - 'a'];
            --dict[t[idx] - 'a'];
        }

        for (std::size_t idx = 0; idx < dict.size(); ++idx)
            if (dict[idx] != 0)
                return false;

        return true;
    }
};

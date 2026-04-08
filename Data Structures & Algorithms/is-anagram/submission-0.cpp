class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
        
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());

        for (std::size_t idx = 0; idx < s.size(); ++idx) {
            if (s[idx] != t[idx])
                return false;
        }

        return true;
    }
};

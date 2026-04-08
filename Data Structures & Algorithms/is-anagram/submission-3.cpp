class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;

        std::unordered_map<char, int> dict;

        for (std::size_t i = 0; i < s.size(); ++i) {
            ++dict[s[i]];
            --dict[t[i]];
            if (dict[t[i]] == 0)
                dict.erase(t[i]);
            
            if (dict[s[i]] == 0)
                dict.erase(s[i]);
        }

        return dict.size() == 0;
    }
};

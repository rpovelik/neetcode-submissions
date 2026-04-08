class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
        
        std::unordered_map<char, std::size_t> dict;

        for (char& c : s)
            dict[c] += 1;

        for (char& c : t) {
            if (dict[c] == 0)
                return false;
            dict[c] -=1;
            if (dict[c] == 0)
                dict.erase(c);
        }

        return dict.size() == 0;
    }
};

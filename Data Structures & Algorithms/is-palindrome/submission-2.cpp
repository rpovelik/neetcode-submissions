class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() < 2)
            return true;
        
        std::size_t first = 0, last = s.size() - 1;

        while (first <= last) {
            while (first < last && !std::isalnum(s[first]))
                ++first;
            while (last > first && !std::isalnum(s[last]))
                --last;

            if (first > last)
                break;

            if (std::tolower(s[first]) != std::tolower(s[last])) {
                return false;
            } else {
                if (first < s.size())
                    ++first;
                if (last > 0)
                    --last;
            }
        }

        return true;
    }
};

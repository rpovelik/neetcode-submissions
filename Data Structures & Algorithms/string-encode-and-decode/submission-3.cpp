class Solution {
public:

    string encode(vector<string>& strs) {
        std::string encoded;

        if (strs.size() == 0)
            return encoded;

        for (const auto& s : strs) {
            encoded += std::to_string(s.size()) + '@';
            encoded += s;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        std::vector<std::string> answer;

        if (s.size() == 0)
            return answer;
        
        auto first = s.begin(), last = s.begin();

        while (last != s.end()) {
            while (*last != '@')
                ++last;
            std::size_t len = std::stoul(s.substr(first - s.begin(), last - first));
            answer.push_back(s.substr(last - s.begin() + 1, len));
            last += len + 1;
            first = last;
        }

        return answer;
    }
};

class Solution {
public:

    string encode(vector<string>& strs) {
        std::string encoded;
        encoded.reserve(100 * 200); // there are not more than 100 strs with not more than 200 chars in each

        std::cout << "ENCODING..." << std::endl;
        for (const auto& str : strs) {
            if (str.size() == 0) {
                encoded += char{0x2};
            } else {
                encoded += str;
                encoded += char{0x1};
            }
        }
        std::cout << "ENCODED" << std::endl;
        return encoded;
    }

    vector<string> decode(string s) {
        std::vector<std::string> answer;

        auto first = s.begin(), last = s.begin();

        while (first != s.end()) {
            // last will never reach end before first, so no need for the check on the end
            while (*last != 0x1 && *last != 0x2)
                ++last;
            if (*last == 0x1) {
                answer.push_back(std::string{first, last});
            } else {
                answer.push_back(std::string{});
            }
            ++last;
            first = last;
        }

        return answer;
    }
};

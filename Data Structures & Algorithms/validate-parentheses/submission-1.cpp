class Solution {
public:
    bool isValid(string s) {
        std::stack<char> opened;
        for (char& c : s) {
            if (c == '{' || c == '(' || c == '[')
                opened.push(c);
            else if(opened.size() > 0) {
                char prev = opened.top();
                opened.pop();
                switch (prev) {
                    case '{':
                        if (c != '}')
                            return false;
                        break;
                    case '[':
                        if (c != ']')
                            return false;
                        break;
                    case '(':
                        if (c != ')')
                            return false;
                        break;
                }
            } else {
                return false;
            }
        }

        return opened.size() == 0;
    }
};

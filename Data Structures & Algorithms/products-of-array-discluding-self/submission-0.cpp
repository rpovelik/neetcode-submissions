std::ostream& operator<<(std::ostream& os, std::vector<int>& vec) {
    for (auto& elem : vec) {
        os << elem << " ";
    }
    return os;
}


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& input) {
        const int size = input.size();
        vector<int> output(size, 1);

        std::cout << output << std::endl;

        for (int i = 1; i < size; ++i)
            output[i] = output[i - 1] * input[i - 1];

        std::cout << output << std::endl;

        for (int i = size - 2; i > 0; --i)
            input[i] *= input[i + 1];

        std::cout << input << std::endl;

        for (int i = 0; i < size - 1; ++i)
            output[i] *= input[i + 1];

        return output;
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int i = 0; i < numbers.size(); ++i) {
            auto it = std::lower_bound(numbers.begin() + i, numbers.end(), (target - numbers[i]));
            if (it == numbers.end())
                continue;
            if (*it != (target - numbers[i]))
                continue;
            return {i + 1, it - numbers.begin() + 1};
        }
        return {};
    }
};

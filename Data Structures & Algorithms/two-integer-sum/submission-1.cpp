class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, std::size_t> unique_nums;

        for (std::size_t idx = 0; idx < nums.size(); ++idx) {
            unique_nums[nums[idx]] = idx;
        }

        for (int idx = 0; idx < nums.size(); ++idx) {
            if (target - nums[idx] < nums[idx])
                continue;
            auto it = unique_nums.find(target - nums[idx]);
            if (it != unique_nums.end() && it->second != idx) {
                int i = it->second;
                return std::vector<int>{std::min(i, idx), std::max(i, idx)};
            }
        }
    }
};

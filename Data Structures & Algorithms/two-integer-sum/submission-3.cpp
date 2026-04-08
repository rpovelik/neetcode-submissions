class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, std::size_t> unique_nums;

        for (std::size_t idx = 0; idx < nums.size(); ++idx) {
            auto it = unique_nums.find(target - nums[idx]);
            if (it != unique_nums.end()) {
                return {it->second, idx};
            }
            unique_nums[nums[idx]] = idx;
        }
    }
};

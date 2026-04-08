class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, std::size_t> num_to_idx;

        for (std::size_t idx = 0; idx < nums.size(); ++idx) {
            int diff = target - nums[idx];
            auto it = num_to_idx.find(diff);
            if (it == num_to_idx.end())
                num_to_idx[nums[idx]] = idx;
            else
                return {it->second, idx};
        }

        return {};
    }
};

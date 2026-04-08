class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, std::vector<std::size_t>> num_to_idx;

        for (std::size_t idx = 0; idx < nums.size(); ++idx) {
            num_to_idx[nums[idx]].push_back(idx);
        }

        for (const auto& p : num_to_idx) {
            auto it = num_to_idx.find(target - p.first);

            if (it != num_to_idx.end()) {
                if (it->second.size() == 1) {
                    return {std::min(p.second[0], it->second[0]), std::max(p.second[0], it->second[0])};
                }
                else {
                    return {std::min(it->second[0], it->second[1]), std::max(p.second[0], it->second[1])};
                }
            }
        }

        return {};
    }
};

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.size() < 2)
            return false;
        std::sort(nums.begin(), nums.end());

        for (std::size_t idx = 1; idx < nums.size(); ++idx) {
            if (nums[idx] == nums[idx - 1]) {
                return true;
            }
        }
        
        return false;
    }
};

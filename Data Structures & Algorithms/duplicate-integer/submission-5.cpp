class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> _set(nums.begin(), nums.end());
        return _set.size() != nums.size();
    }
};
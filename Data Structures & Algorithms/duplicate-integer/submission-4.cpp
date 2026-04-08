class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> _set;
        for (auto num : nums) {
            if (_set.count(num) == 1)
                return true;
            else
                _set.insert(num);
        }
        return false;
    }
};
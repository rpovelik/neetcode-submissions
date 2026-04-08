class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> unique;
        for (int& num : nums) {
            auto res = unique.insert(num);
            if (!res.second)
                return true;
        }
        return false;
    }
};

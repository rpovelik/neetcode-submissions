class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto left = nums.begin();
        std::size_t len = nums.size();

        while (len > 0) {
            std::size_t half = len >> 1;
            auto middle = left + half;

            if (*middle < target) {
                left = middle + 1;
                len -= half + 1;
            } else {
                len = half;
            }
        }

        if (left == nums.end())
            return -1;
        
        return *left == target ? left - nums.begin() : -1;
    }
};

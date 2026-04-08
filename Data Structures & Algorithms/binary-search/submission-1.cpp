class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto left = nums.begin();
        std::size_t dist = nums.size();

        while (dist > 0) {
            std::size_t half = dist >> 1;
            auto mid = left + half;

            if (*mid < target) {
                dist -= half + 1;
                left = mid + 1;
            } else {
                dist = half;
            }
        }

        if (left == nums.end())
            return -1;
        
        return *left == target? left - nums.begin() : -1;
    }
};

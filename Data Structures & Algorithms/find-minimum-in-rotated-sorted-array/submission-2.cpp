class Solution {
public:
    int findMin(vector<int> &nums) {
        auto left = nums.begin(), right = nums.end() - 1;
        int min = *left;
        
        while (left <= right) {
            if (*left < *right)
                return std::min(*left, min);
            
            std::size_t dist = std::distance(left, right);
            std::size_t half = dist >> 1;
            auto mid = left + half;
            min = std::min(*mid, min);

            if (*mid >= *left) { // equal to cover the case when left and mid points to the same
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return min;
    }
};

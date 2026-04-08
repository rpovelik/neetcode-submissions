class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> answer;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) // it's positive, so we won't find negative further to get 0
                break;
            if (i > 0 && nums[i] == nums[i - 1]) // it's identical to prev, but we don't need duplicates
                continue;
            
            // let's use two sum algorithm for the rest of nums
            int l = i + 1, r = nums.size() - 1;

            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum > 0)
                    --r;
                else if (sum < 0)
                    ++l;
                else {
                    answer.push_back({nums[i], nums[l], nums[r]});
                    ++l;
                    --r;
                    while (l < r && nums[l] == nums[l - 1])
                        ++l;
                }
            }
        }
        return answer;
    }
};

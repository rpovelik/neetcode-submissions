class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> set(nums.begin(), nums.end());
        int answer = 0;

        for (const auto& num : nums) {
            if (set.count(num - 1) == 0) {
                int length = 1;
                
                while (set.count(num + length))
                    ++length;
                
                answer = std::max(length, answer);
            }
        }

        return answer;
    }
};

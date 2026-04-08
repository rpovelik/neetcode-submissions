class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> num_to_freq;

        for (auto& num : nums)
            ++num_to_freq[num];

        std::vector<std::vector<int>> freq_to_num(nums.size() + 1);

        for (auto& pair : num_to_freq) {
            freq_to_num[pair.second].push_back(pair.first);
        }

        std::vector<int> answer;
        answer.reserve(k);

        for (auto r_it = freq_to_num.rbegin(); r_it != freq_to_num.rend(); ++r_it) {
            for (auto& num : *r_it) {
                answer.push_back(num);
                if (answer.size() == k)
                    return answer;
            }
        }

        return answer;
    }
};

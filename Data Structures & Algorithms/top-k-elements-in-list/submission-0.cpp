class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> answer;
        std::unordered_map<int, int> freq;
        std::map<int, std::vector<int>, std::greater<int>> sorted_freq;

        for (int& num : nums)
            ++freq[num];
        
        answer.reserve(k);
        
        for (auto& pair : freq)
            sorted_freq[pair.second].push_back(pair.first);
        
        for (auto& pair : sorted_freq)
            for (auto& num : pair.second) {
                answer.push_back(num);
                if (answer.size() == k)
                    return answer;
            }
    }
};

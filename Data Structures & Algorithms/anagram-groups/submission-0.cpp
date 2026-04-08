class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> answer;
        unordered_map<string, std::vector<std::string>> hash_map;

        for (string& s : strs) {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());
            hash_map[sorted_s].push_back(s);
        }

        for (auto& bucket : hash_map) {
            answer.push_back(bucket.second);
        }

        return answer;
    }
};

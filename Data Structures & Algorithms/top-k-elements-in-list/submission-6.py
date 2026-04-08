class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []

        num_to_freq = {}
        min_f, max_f = float("inf"), 0

        for num in nums:
            num_to_freq[num] = 1 + num_to_freq.get(num, 0)
            min_f = min(num_to_freq[num], min_f)
            max_f = max(num_to_freq[num], max_f)
        print(min_f, max_f)
        freq_to_num = [[] for _ in range(0, len(nums) + 1)]

        for num, f in num_to_freq.items():
            print(f)
            freq_to_num[f].append(num)

        for i in range(len(nums), 0, -1):
            for num in freq_to_num[i]:
                answer.append(num)
                k -= 1
                if k == 0:
                    return answer
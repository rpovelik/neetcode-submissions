from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        print(buckets)
        print(freqs)
        for num, freq in freqs.items():
            print(num, freq)
            buckets[freq].append(num)
        
        print(buckets)
        res = []
        for idx in range(len(nums), -1, -1):
            for num in buckets[idx]:
                res.append(num)
                if (len(res) == k):
                    return res
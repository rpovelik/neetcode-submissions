class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []

        key_freq = {}

        for num in nums:
            key_freq[num] = 1 + key_freq.get(num, 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, freq in key_freq.items():
            buckets[freq].append(key)

        for bucket in reversed(buckets):
            if len(bucket) == 0:
                continue
            else:
                for key in bucket:
                    if k > 0:
                        k -= 1
                        answer.append(key)
                    else:
                        return answer 

        return answer
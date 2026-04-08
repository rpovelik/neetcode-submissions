class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        answer = 0

        for num in nums:
            if num - 1 not in s:
                tmp = num + 1
                while tmp in s:
                    tmp += 1
                answer = max(tmp - num, answer)
            else:
                continue
        
        return answer
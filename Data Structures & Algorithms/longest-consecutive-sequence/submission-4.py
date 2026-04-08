class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        answer = 0

        for num in nums:
            if num - 1 not in lookup:
                tmp = num + 1
                while tmp in lookup:
                    tmp += 1
                answer = max(answer, tmp - num)

        return answer

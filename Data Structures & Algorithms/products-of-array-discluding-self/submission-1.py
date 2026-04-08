class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, post, res = [1 for _ in nums], [1 for _ in nums], [1 for _ in nums]

        pref[0] = nums[0]
        post[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(1, len(nums)):
            pref[i] = nums[i] * pref[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i] * post[i + 1]
        print(pref)
        print(post)
        for i in range(len(nums)):
            if i == 0:
                res[i] = post[i + 1]
            elif i == len(nums) -1:
                res[i] = pref[i - 1]
            else:
                res[i] = post[i + 1] * pref[i - 1]

        return res
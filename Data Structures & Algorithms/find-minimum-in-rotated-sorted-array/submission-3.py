class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1

        while s < e:
            diff = (e - s) // 2
            mid = s + diff

            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid

        return nums[s]
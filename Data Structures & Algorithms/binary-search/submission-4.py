class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            diff = (e - s) // 2
            mid = s + diff
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        
        return -1
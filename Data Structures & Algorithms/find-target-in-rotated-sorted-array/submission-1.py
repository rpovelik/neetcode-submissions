class Solution:
    def search(self, nums: List[int], t: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            diff = (e - s) // 2
            mid = s + diff
            if nums[mid] == t:
                return mid

            if nums[mid] < nums[e]:
                if nums[mid] < t <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1
            else:
                if nums[s] <= t < nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
        
        return -1
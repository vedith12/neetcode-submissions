class Solution:
    def binarySearch(self, nums, t, leftBias):
        l = 0
        r = len(nums) - 1
        i = -1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == t:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] > t:
                r = m - 1
            else:
                l = m + 1
        return i
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]
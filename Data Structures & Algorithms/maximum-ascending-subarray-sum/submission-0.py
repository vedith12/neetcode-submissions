class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        currsum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                currsum = 0
            currsum += nums[i]
            res = max(res, currsum)
        return res
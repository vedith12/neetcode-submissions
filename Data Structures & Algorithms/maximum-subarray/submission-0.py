class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxi = float('-inf')
        for i in range(len(nums)):
            currsum += nums[i]
            maxi = max(currsum, maxi)
            if currsum < 0:
                currsum = 0
        return maxi
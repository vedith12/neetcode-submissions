class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        count[0] = 1
        prefixSum, res = 0, 0

        for num in nums:
            prefixSum += num
            if prefixSum >= goal:
                res += count[prefixSum - goal]
            count[prefixSum] += 1

        return res
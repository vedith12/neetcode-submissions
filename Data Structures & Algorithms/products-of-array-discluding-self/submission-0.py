class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        endlist = []
        for i in range(len(nums)):
            prod = 1
            for x in nums[:i] + nums[i+1:]:
                prod *= x
            endlist.append(prod)
        return endlist
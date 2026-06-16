class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #here the approach is that i will reverse the entire array first, then reverse only the first K elements then reverse the remaining len(nums) - k elements
        #without defining reverse function
        n = len(nums)
        k %= n

        nums[:] = nums[n-k:] + nums[:n-k]

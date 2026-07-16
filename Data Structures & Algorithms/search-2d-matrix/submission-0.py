class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [item for sublist in matrix for item in sublist]
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return False
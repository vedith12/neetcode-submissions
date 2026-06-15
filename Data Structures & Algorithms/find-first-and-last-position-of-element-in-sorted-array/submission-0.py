class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstOccurrence(nums, target):
            low, high = 0, len(nums) -1
            first = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] == target:
                    first = mid
                    high = mid-1 #endukante i want to find the first occurrence, it can be available in the left side thats why 
                elif target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            return first
        def lastOccurrence(nums, target):
            low, high = 0, len(nums) -1
            last = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid] == target:
                    last = mid
                    low = mid+1 #endukante i want to find the last occurrence, it can be available in the right side thats why 
                elif target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            return last
        first = firstOccurrence(nums, target)
        last = lastOccurrence(nums, target)
        return [first, last]
  

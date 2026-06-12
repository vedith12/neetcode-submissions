class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        currsum = 0
        totalcount = 0
        for i in range(len(nums)):
            currsum += nums[i]
            sub = currsum - k
            if sub in hashmap:
                totalcount += hashmap[sub]
            hashmap[currsum] = hashmap.get(currsum,0)+1
        return totalcount
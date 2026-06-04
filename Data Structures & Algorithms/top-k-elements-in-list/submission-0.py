class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        items = sorted(hashmap.items(), reverse = True, key = lambda item: item[1])
        ans = []
        for i in range(k):
            ans.append(items[i][0])
        return ans
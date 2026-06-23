class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        #to get the maximum difference, i need max odd, and min even
        maxodd = 0
        mineven = float('inf')
        for i in counts:
            if counts.get(i,0) %2 == 1:
                maxodd = max(maxodd, counts.get(i,0))
            elif counts.get(i,0)%2 == 0:
                mineven = min(mineven, counts.get(i,0))
        return maxodd-mineven

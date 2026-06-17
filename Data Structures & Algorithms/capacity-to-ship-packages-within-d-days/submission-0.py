class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def isValid(mid):
            daysNeeded = 1
            currweight = 0
            for w in weights:
                if currweight + w >mid:
                    daysNeeded +=1
                    currweight = w
                else:
                    currweight += w
            return daysNeeded <= days
        
        while l<=r:
            m = (l+r)//2
            if isValid(m):
                r = m-1
            else:
                l = m +1
        return l


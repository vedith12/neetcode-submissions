class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1, n
        res = 0
        while l<= r:
            mid = (l+r)//2
            if mid*(mid+1)//2 <=n:
                res = mid 
                l = mid+1
            else:
                r = mid-1

        return res
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        res = ""
        for r in range(2, len(num)):
            if num[l]== num[l+1] == num[r]:
                res = max(res, num[l:r+1])
            l+=1
        return res
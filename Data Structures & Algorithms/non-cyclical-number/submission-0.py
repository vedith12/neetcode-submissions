class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!= 1:
            if n in seen:
                return False
            seen.add(n)
            sumvar = 0
            for num in str(n):
                sumvar += int(num) **2
            n= sumvar
        return True


class Solution:
    def minOperations(self, s: str) -> int:
        ops = 0
        for i in range(len(s)):
            if i%2 == 1:
                if s[i] == "1":
                    ops += 1
            if i%2 == 0:
                if s[i] == "0":
                    ops +=1
        return min(ops, len(s)-ops)
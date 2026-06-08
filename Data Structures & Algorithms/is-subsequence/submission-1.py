class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #bruteforce
        a = []
        index = 0
        for char in s:
            for i in range(index, len(t)):
                if char == t[i]:
                    a.append(True)
                    index = i + 1
                    break
        return len(a) == len(s)
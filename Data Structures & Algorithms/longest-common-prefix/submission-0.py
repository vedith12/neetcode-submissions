class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        shortest = min(strs, key = len)
        i = 0
        while i < len(shortest):
            for s in strs:
                if s[i] != shortest[i]:
                    return res
            res+= s[i]
            i+=1
        return res

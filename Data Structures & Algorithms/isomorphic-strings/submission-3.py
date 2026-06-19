from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}
        for i in range(len(s)):
            chS, chT = s[i], t[i]
            if (chS in hashmapS and hashmapS[chS] != chT) or (chT in hashmapT and hashmapT[chT] != chS):
                return False
            hashmapS[chS] = chT
            hashmapT[chT] = chS
        return True

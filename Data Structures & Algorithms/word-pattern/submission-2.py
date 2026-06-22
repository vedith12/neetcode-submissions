class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        if len(pattern) != len(slist):
            return False
        
        p2w = {}
        w2p = {}
        i = 0
        while i<len(pattern):
            p = pattern[i]
            w = slist[i]
            if p in p2w and p2w[p] != w:
                return False
            if w in w2p and w2p[w] != p:
                return False
            p2w[p] = w
            w2p[w] = p
            i+=1
        return True
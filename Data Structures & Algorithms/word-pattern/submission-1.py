class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pset = set(pattern)
        s = s.split()
        sset = set(s)
        if len(pset) == len(sset) and len(s) == len(pattern):
            return True
        else:
            return False
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        spointer = 0
        tpointer = 0
        while spointer < len(s) and tpointer<len(t):
            if s[spointer] == t[tpointer]:
                tpointer +=1
            spointer +=1
        return len(t[tpointer:])
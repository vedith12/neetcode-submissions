class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        if len(pattern) != len(slist):
            return False
        
        hashmap = {}
        seen = set()
        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                if slist[i] in seen:
                    return False
                hashmap[pattern[i]] = slist[i]
                seen.add(slist[i])
            else:
                if hashmap[pattern[i]]!= slist[i]:
                    return False
        return True

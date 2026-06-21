class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:    
        allowedmap = set(allowed)
        res = 0
        for word in words:
            valid = True
            for ch in word:
                if ch not in allowedmap:
                    valid = False
                    break
                
            if valid:
                res +=1
        return res

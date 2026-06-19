class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = list(magazine)
        for ch in ransomNote:
            if ch not in m:
                return False
            else:
                m.remove(ch)
        return True
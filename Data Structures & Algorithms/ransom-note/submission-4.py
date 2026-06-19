class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDih = Counter(ransomNote)
        magazineDih = Counter(magazine)
        for ch in ransomDih:
            if magazineDih[ch] < ransomDih[ch]:
                return False
        return True
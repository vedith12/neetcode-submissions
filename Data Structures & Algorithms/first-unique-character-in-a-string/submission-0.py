class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for ch in range(len(s)):
            if counts[s[ch]] ==1:
                return ch
        return -1
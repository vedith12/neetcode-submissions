class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        balloon = Counter("balloon")
        res = float('inf')
        for ch in balloon:
            res = min(res, counts[ch]//balloon[ch])
        return res
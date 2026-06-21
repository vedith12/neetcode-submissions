class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        oddch = False
        length = 0
        for ch in counts:
            if counts[ch] %2 == 0:
                length += counts[ch]
            else:
                length += counts[ch] -1
                oddch = True
        if oddch :
            length +=1
        return length

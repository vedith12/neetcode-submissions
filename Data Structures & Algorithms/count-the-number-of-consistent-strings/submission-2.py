class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedset = set(allowed)
        count = 0

        for word in words:
            if all(ch in allowedset for ch in word):
                count += 1

        return count
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = Counter(chars)
        res = 0

        for word in words:
            if Counter(word) <= chars_cnt:
                res += len(word)

        return res
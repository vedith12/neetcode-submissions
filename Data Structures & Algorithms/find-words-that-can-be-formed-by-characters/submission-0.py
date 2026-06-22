class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        for word in words:
            cnt = Counter(chars)
            valid = True

            for ch in word:
                if cnt[ch] == 0:
                    valid = False
                    break
                cnt[ch] -= 1

            if valid:
                res += len(word)

        return res
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        distinct = 0
        for string in arr:
            if counts[string] == 1:
                distinct +=1
            if distinct == k:
                return string
        return ""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in frequency:
                frequency[key].append(i)
            else:
                frequency[key] = [i]
        result = []
        for i in frequency.values():
            result.append(i)
        return result
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        for x, y in zip(names, heights):
            dic[y] = x
        res = []
        for ppl in reversed(sorted(heights)):
            res.append(dic[ppl])
        return res
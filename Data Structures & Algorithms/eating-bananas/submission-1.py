class Solution:
    def minEatingSpeed(self, piles: List[int], h: int):

        def isValid(mid):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            return hours <= h

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if isValid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
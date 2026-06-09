class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        for i in range(len(height)):
            maxleft = max(height[:i+1])
            maxright = max(height[i:])
            area += min(maxleft, maxright) - height[i]
        return area

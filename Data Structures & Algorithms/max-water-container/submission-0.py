class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights)-1
        max_limit = 0
        while l < r:
            water_limit = min(heights[l], heights[r]) * (r-l)
            max_limit = max(max_limit, water_limit)

            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return max_limit
        
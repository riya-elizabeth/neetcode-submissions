class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = [0]*len(height)
        curr_max_left = 0
        for i in range(len(height)):
            max_left[i] = curr_max_left
            curr_max_left = max(curr_max_left, height[i])
        
        max_right = [0]* len(height)
        curr_max_right = 0
        for i in range(len(height)-1,-1,-1):
            max_right[i] = curr_max_right
            curr_max_right = max(curr_max_right, height[i])
        
        total = 0
        for i in range(len(height)):
            total = total + max(0,(min(max_left[i], max_right[i])- height[i]))
        return total
        
class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_water = 0
        while(i<j):
            width = j - i
            area = min(height[i], height[j]) * width
            max_water = max(max_water, area)
            if height[i] < height [j]:
                i += 1
            else:
                j -= 1
        return max_water
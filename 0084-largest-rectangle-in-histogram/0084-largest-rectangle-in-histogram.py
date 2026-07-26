class Solution(object):
    def largestRectangleArea(self, heights):
        rectangle_area = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                rectangle_area = max(rectangle_area, height*width)
            stack.append(i)
        return rectangle_area

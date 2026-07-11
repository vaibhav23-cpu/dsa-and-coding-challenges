class Solution(object):
    def trap(self, height):
        i = 0
        j = len(height)-1
        i_max = 0
        j_max = 0
        water = 0
        while i < j:
            if height[i] < height [j]:
                if height[i] >= i_max:
                    i_max = height[i]
                else:
                    water += i_max - height[i]
                i += 1
            else:
                if height[j] >= j_max:
                    j_max = height[j]
                else:
                    water += j_max - height[j]
                j -= 1
                
        return water
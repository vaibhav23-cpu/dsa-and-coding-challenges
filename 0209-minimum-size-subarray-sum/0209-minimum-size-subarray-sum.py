class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        res = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(right-left+1,res)
                total -= nums[left]
                left +=1
        if res == float('inf'):
            return 0
        return res
        
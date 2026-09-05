class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = 0
        one = 0
        seen = {}
        res = 0
        for i in range(len(nums)):
            if(nums[i]==0):
                zero += 1
            else:
                one += 1
            diff = zero - one
            if diff == 0:
                res = max(res,i+1)
                continue
            if diff in seen:
                index = seen[diff]
                arr_len = i-index
                res = max(arr_len,res)
            else:
                seen[diff] = i
        return res       
class Solution(object):
    def subarraysDivByK(self, nums, k):
        sum_num = 0
        seen = {0:1}
        res = 0
        for i in range(len(nums)):
            sum_num += nums[i]
            rem = sum_num % k
            if rem < 0:
                rem = rem + k
            if rem in seen:
                res += seen[rem]
            seen[rem] = seen.get(rem, 0) + 1
        return res
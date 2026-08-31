class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)
        a = nums
        max_sum = a[0]
        min_sum = a[0]
        current_max = a[0]
        current_min = a[0]
        for i in range(1, len(nums)):
            current_max = max(a[i], current_max+a[i])
            max_sum = max(max_sum, current_max)

            current_min = min(a[i], current_min+a[i])
            min_sum = min(min_sum, current_min)

        if max_sum < 0:
            return max_sum
        return max(max_sum, total-min_sum)
        
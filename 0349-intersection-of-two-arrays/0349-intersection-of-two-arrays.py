class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        answer = set()
        for num in nums2:
            if num in seen:
                answer.add(num)
        return list(answer)
        
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        left =0
        window = set()
        for right in range(len(nums)):
            if nums[right] in window:
                return True
            window.add(nums[right])
            if right - left >= k:
                window.remove(nums[left])
                left +=1
        return False
        
class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        n = len(nums)
        answer = [-1]*n
        for i in range(2*n):
            index = i%n
            while stack and nums[index] > nums[stack[-1]]:
                prev = stack.pop()
                answer[prev] = nums[index]
            if i < n:
                stack.append(index)
        return answer
        
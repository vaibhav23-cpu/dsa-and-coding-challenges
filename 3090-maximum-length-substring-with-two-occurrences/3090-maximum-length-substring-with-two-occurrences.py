class Solution(object):
    def maximumLengthSubstring(self, s):
        left = 0
        longest = 0
        freq = {}
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right] , 0) + 1
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left +=1
            longest = max(longest,right-left+1)
        return longest


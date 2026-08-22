class Solution(object):
    def minWindow(self, s, t):
        low = 0
        have = 0
        freq = {}
        need = {}
        for char in t:
            need[char] = need.get(char,0)+1
        need_count = len(need)
        min_len = float("inf")
        start = 0

        for high in range(len(s)):

            if s[high] in need:
                freq[s[high]] = freq.get(s[high],0)+1

                if freq[s[high]] == need[s[high]]:
                    have+=1
            while have == need_count:
                length = high - low+1
                if min_len > length:
                    min_len = length
                    start = low
                if s[low] in need:
                    if freq[s[low]] == need[s[low]]:
                        have-=1
                    freq[s[low]]-=1
                low+=1
        if min_len == float("inf"):
            return ""

        return s[start:start+min_len]
            

        
class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        left = 0
        res = 0
        freq = {}
        max_freq = 0
        for right in range(n):
            freq[s[right]] = freq.get(s[right],0)+1    #high ko information m liya
            max_freq = max(max_freq, freq[s[right]])   
            while (right - left +1) - max_freq >k:    #low ko shrink kiya jabtak statement theek nhi hota fir low ko delete krdya freq se
                freq[s[left]] -=1
                if freq[s[left]] == 0:      
                    del freq[s[left]]
                left +=1
            size = right-left +1
            res = max(res,size)
        return res
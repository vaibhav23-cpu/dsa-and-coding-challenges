class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        ans = [ 0 ]*n
        if k ==0:
            return ans

        if k > 0:
            window_sum = 0
            for j in range(1, k+1):
                window_sum += code[j%n]
            for i in range(n):
                ans[i] = window_sum
                window_sum -= code[(i+1)%n]
                window_sum += code[(i+k+1)%n]
        else:
            k = abs(k)
            window_sum = 0
            for j in range(1, k+1):
                window_sum += code[-j]
                for i in range(n):
                    ans[i] = window_sum
                    window_sum -= code[(i-k)%n]
                    window_sum += code[i] 
        return ans
        
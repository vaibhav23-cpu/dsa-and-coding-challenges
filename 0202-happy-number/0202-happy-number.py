class Solution(object):
    def isHappy(self, n):
        def nextNumber(n):
            total = 0
            while (n>0):
                d = n%10
                n = n//10
                total = total + d*d
            return total
        slow = n
        fast = n
        while(fast !=1):
            slow = nextNumber(slow)
            fast = nextNumber(nextNumber(fast))
            if slow == fast and slow !=1:
                return False
        return True

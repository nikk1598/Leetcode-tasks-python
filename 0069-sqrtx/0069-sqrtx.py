class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        elif x == 2:
            return 1
        for n in range(0, x):
            if n*n > x:
                return n-1
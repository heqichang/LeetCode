class Solution:
    def myPow(self, x: float, n: int) -> float:

        res = 1.0
        m = abs(n)
        while m != 0:
            if m % 2 != 0:
                res *= x
            x *= x
            m //= 2
            print(m)
        return res if n >= 0 else 1 / res


# 1 分治，看题解的，2^10 = 2^5 * 2^5 来解决


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        num = abs(x)
        l = []
        s = ''
        while num != 0:
            a = num % 10
            num = int(num / 10)
            l.append(str(a))
        s = s.join(l)
        r = int(s)
        if x < 0:
            r = -r
        if r > 2147483647:
            return 0
        elif r < -2147483648:
            return 0
        else:
            return r

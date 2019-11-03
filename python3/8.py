class Solution:
    def myAtoi(self, str: str) -> int:

        tmp = str.strip()
        if len(tmp) == 0:
            return 0

        factor = 1
        start = 0
        nums = []
        if tmp[0] == '-':
            factor = -1
            start = 1
        if tmp[0] == '+':
            factor = 1
            start = 1
        for c in range(start, len(tmp)):
            o = ord(tmp[c])
            if o >= 48 and o <= 57:
                nums.append(int(tmp[c]))
            else:
                break

        nums.reverse()

        if len(nums) == 0:
            return 0

        max_num = pow(2, 31)

        if factor == 1:
            max_num -= 1

        num = 0

        for i in range(0, len(nums)):
            num += (nums[i] * pow(10, i))
            if num > max_num:
                num = max_num
                break

        return factor * num

class Solution:
    def intToRoman(self, num: int) -> str:

        s = ''
        l = [
            ['I', 'V'],
            ['X', 'L'],
            ['C', 'D'],
            ['M']
        ]

        index_l = 0
        while num != 0:
            mod = num % 10
            if mod < 4:
                for i in range(mod):
                    s = l[index_l][0] + s
            elif mod == 4:
                s = l[index_l][0] + l[index_l][1] + s
            elif mod < 9:
                temp = l[index_l][1]
                for i in range(mod - 5):
                    temp += l[index_l][0]
                s = temp + s
            else:
                s = l[index_l][0] + l[index_l + 1][0] + s

            index_l += 1
            num = num // 10

        return s

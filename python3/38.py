class Solution:
    def countAndSay(self, n: int) -> str:

        begin = '1'

        if n == 1:
            return begin

        nextStr = begin
        for i in range(n - 1):
            lastChar = nextStr[0]
            count = 0
            temp = ''

            for c in range(len(nextStr)):
                if nextStr[c] == lastChar:
                    count += 1
                else:
                    temp = temp + str(count)
                    temp = temp + lastChar
                    lastChar = nextStr[c]
                    count = 1

            temp += str(count)
            temp += nextStr[len(nextStr) - 1]
            nextStr = temp

        return nextStr


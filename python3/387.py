class Solution:
    def firstUniqChar(self, s: str) -> int:

        length = len(s)

        if length == 0:
            return -1

        dic = {}

        for i in range(length):
            c = s[i]
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        for i in range(length):
            c = s[i]
            if dic[c] == 1:
                return i

        return -1

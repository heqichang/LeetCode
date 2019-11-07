from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        length = len(strs)

        if length == 0:
            return ''

        if length == 1:
            return strs[0]

        min_length = len(strs[0])
        min_index = 0
        for i in range(1, len(strs)):
            if len(strs[i]) < min_length:
                min_length = len(strs[i])
                min_index = i

        last = 0
        duplicate = True
        for i in range(0, min_length):

            if duplicate:
                for j in range(1, len(strs)):

                    if strs[j - 1][i] != strs[j][i]:
                        duplicate = False
                        break
                if duplicate:
                    last += 1

            else:
                break

        return strs[min_index][0:last]

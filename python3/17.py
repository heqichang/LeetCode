from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        mid = []
        for i in range(len(digits)):
            chars = d[digits[i]]
            if len(mid) == 0:
                for j in range(len(chars)):
                    mid.append(chars[j])
            else:
                temp_mid = []
                for j in range(len(chars)):
                    for k in range(len(mid)):
                        temp_mid.append(mid[k] + chars[j])
                mid = temp_mid

        # mid.sort() # 为了在线对比结果的
        return mid


# 1 定义好字典，暴力解决
# 2 递归

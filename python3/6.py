class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        cur = 0
        down = False
        for c in s:
            rows[cur] += c
            if cur == 0 or numRows - cur == 1:
                down = (down == False)
            cur += (1 if down else -1)

        result = ''
        for item in rows:
            result += item
        return result

# 1 看题解的，循环数组，用字母去填充

class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self._generate(0, 2 * n, '', result)
        return result

    def _generate(self, level: int, max_level: int, s: str, res: List[str]):

        if level == max_level:
            if self._valide(s):
                res.append(s)
            return

        self._generate(level + 1, max_level, s + '(', res)
        self._generate(level + 1, max_level, s + ')', res)

    def _valide(self, s: str) -> bool:

        l = '('
        r = ')'
        count = 0
        for c in s:
            if c == l:
                count += 1
            else:
                count -= 1

            if count < 0:
                return False

        return count == 0


# 看题解有更优解法

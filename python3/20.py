class Solution:
    def isValid(self, s: str) -> bool:
        left = ('(', '[', '{')
        right = (')', ']', '}')

        stack = []

        for i in range(len(s)):
            c = s[i]
            if c in left:
                stack.append(left.index(c))
            elif c in right:
                if len(stack) == 0:
                    return False

                r = right.index(c)

                if r == stack[-1]:
                    stack.pop()
                else:
                    return False

        if len(stack) != 0:
            return False

        return True




class Solution:
    # AC
    def removeDuplicates(self, S: str) -> str:

        s_len = len(S)

        if s_len == 0 or s_len == 1:
            return S

        stack = [S[0]]

        for i in range(1, s_len):
            if len(stack) == 0 or stack[-1] != S[i]:
                stack.append(S[i])
            else:
                stack.pop()

        return ''.join(stack)

    # wrong answer
    def removeDuplicates2(self, S: str) -> str:

        s_len = len(S)

        if s_len == 0 or s_len == 1:
            return S

        stack = [S[0]]
        need_pop = False

        for i in range(1, s_len):

            if need_pop:
                if stack[-1] != S[i]:
                    stack.pop()
                    if len(stack) == 0 or stack[-1] != S[i]:
                        stack.append(S[i])
                        need_pop = False
            else:
                if stack[-1] != S[i]:
                    stack.append(S[i])
                else:
                    need_pop = True

        if need_pop:
            stack.pop()

        return ''.join(stack)


sol = Solution()
sol.removeDuplicates('abbaca')

# 1 用栈，当前元素和栈顶的一样，不入栈，没有重复的了，就出栈一个
# 审题错误，两两重复就应该删除，比如 aaa, 应该只删除 前两个 aa ,保留最后的 a


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = len(s)

        if length == 0:
            return 0

        sub = [s[0]]
        max_length = 0

        for c in s:
            if c in sub:
                if max_length < len(sub):
                    max_length = len(sub)
                while c in sub:
                    sub.pop(0)
                sub.append(c)
            else:
                sub.append(c)

        if max_length < len(sub):
            max_length = len(sub)

        return max_length


    def lengthOfLongestSubstring2(self, s: str) -> int:

        length = len(s)

        if length == 0 or length == 1:
            return length


        max_length = 0
        hash = {}
        begin = 0
        for end in range(length):
            if s[end] in hash:
                begin = max(hash[s[end]], begin)
            max_length = max(max_length, end - begin + 1)
            hash[s[end]] = end + 1

        return max_length

# 1 自写，类似一个队列
# 2 看题解的，滑动窗口

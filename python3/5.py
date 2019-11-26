class Solution:
    def longestPalindrome(self, s: str) -> str:

        length = len(s)
        if length == 0 or length == 1:
            return s

        x = ''

        for i in range(length):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)

            if len(s1) > len(x):
                x = s1
            if len(s2) > len(x):
                x = s2

        return x

    def palindrome(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]


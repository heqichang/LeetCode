class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 0-9 48-57
        # a-z 97-122
        s_list = []
        for c in s.lower():
            a = ord(c)
            if (a >= 48 and a <= 57) or (a >= 97 and a <= 122):
                s_list.append(c)
        return s_list == s_list[::-1]

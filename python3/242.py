class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1

        if len(s_dict) != len(t_dict):
            return False

        for k, v in s_dict.items():
            if k not in t_dict:
                return False
            if v != t_dict[k]:
                return False

        return True

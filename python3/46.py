from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)

        if length == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            temp = nums[:]
            del temp[i]
            sub = self.permute(temp)
            for item in sub:
                result.append([nums[i]] + item)

        return result

# 1 递归，化成小问题

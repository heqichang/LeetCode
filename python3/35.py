from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i in range(len(nums) - 1, -1, -1):
            if target > nums[i]:
                return i + 1
        return 0

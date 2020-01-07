class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        result = nums[0] + nums[1] + nums[2]
        length = len(nums)

        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if (i != j and i != k and j != k):
                        s = nums[i] + nums[j] + nums[k]
                        if abs(target - s) < abs(target - result):
                            result = s

        return result

# 1 暴力 会超时
# 2

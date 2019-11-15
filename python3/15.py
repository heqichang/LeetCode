from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)

        if not nums or length < 3:
            return []

        result = []
        nums.sort()

        for k in range(len(nums) - 2):
            i = k + 1
            j = len(nums) - 1
            target = -nums[k]

            if target < 0:
                break

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            while i < j:

                sum_num = nums[i] + nums[j]
                if sum_num == target:

                    result.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif sum_num < target:
                    i += 1
                elif sum_num > target:
                    j -= 1

        return result


s = Solution()
i = s.threeSum([-1, 0, 1, 2, -1, -4])
print(i)
# 1 暴力，三重循环遍历
# 2 两重循环，最后那个数可判断 减数 是否包含在数组里 (语言内部函数可能还是会循环遍历)
# 3 （题解看到的）x + y = -z ，固定一个 z ，两个指针前后走
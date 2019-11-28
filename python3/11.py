class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        i = 0
        j = len(height) - 1

        while i != j:
            area = min(height[i], height[j]) * (j - i)
            if area > max_area:
                max_area = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area

    # 暴力 超时
    def maxArea2(self, height: List[int]) -> int:

        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area
        return max_area
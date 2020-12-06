"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针的做法
        result = 0
        left, right = 0, len(height) - 1
        tmp = 0
        while left <= right:
            min_l_f = min(height[left], height[right])
            if min_l_f > tmp:
                result += (min_l_f - tmp) * (right - left + 1)
                tmp = min_l_f
            while left <= right and height[left] <= tmp:
                left += 1
            while left <= right and height[right] <= tmp:
                right += 1
        rertun(result - sum(height))

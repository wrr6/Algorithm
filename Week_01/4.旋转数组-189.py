"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        #1.暴力解法,插入时间复杂为n,pop()时间复杂度为1，循环k次，时间复杂度为O(n*k)
        for i in range(k):
            nums.insert(0, nums.pop())

        #2.切片，时间复杂度为O(n)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k] 
        """
        # 3.将每个元素放到对应的位置
        if not k or k <= 0: return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        print(nums)
        self.reverse(nums, end - k + 1, end)
        print(nums)
        self.reverse(nums, 0, end)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

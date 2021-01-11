class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            sums, cnt = 0, 1
            for i in nums:
                if sums + i > mid:
                    cnt += 1
                    sums = i
                else:
                    sums += i
            if cnt <= m:
                r = mid
            else:
                l = mid + 1
        return l
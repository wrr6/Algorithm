"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

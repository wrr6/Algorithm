class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        # print(nums)

        ##明显用回溯法:
        res = []

        def backtrace(nums_b,curr_res,index):
            # print("curr_res:",curr_res)
            if len(curr_res)==k:
                res.append(curr_res[:]) ##浅拷贝，这一步很重要
                return

            for i in range(index,n):
                # print(i,nums_b)
                curr_res.append(nums[i])
                backtrace(nums_b[index:],curr_res,i+1)
                curr_res.pop()

        ##特殊情况处理
        if n==0 or k==0:
            return res

        backtrace(nums,[],0)
        return res

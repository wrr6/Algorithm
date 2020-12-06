"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0]==0:
            digits[-1]+=1
            return digits
        else:
            res=1
            for i in range(len(digits)):
                res+=pow(10,i)*digits[len(digits)-1-i]
        return [int(i) for i in str(res)]
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
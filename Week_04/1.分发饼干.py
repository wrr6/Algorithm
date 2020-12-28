class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_left, s_left, num = 0, 0, 0
        while g_left < len(g) and s_left < len(s):
            if g[g_left] <= s[s_left]:
                g_left += 1
                s_left += 1
                num += 1
            else:
                s_left += 1
        return num
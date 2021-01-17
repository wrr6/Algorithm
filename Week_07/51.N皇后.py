class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 回溯法
        res = []
        s = '.' * n

        def backtrack(path=[], i=0, col_selected=[], z_diag=set(), f_diag=set()):
            if i == n:
                res.append(path)
                return
            for j in range(n):
                if j not in col_selected and i - j not in z_diag and i + j not in f_diag:
                    backtrack(path + [s[:j] + 'Q' + s[j + 1:]], i + 1, col_selected + [j], z_diag | {i - j},
                              f_diag | {i + j})

        backtrack()
        return res
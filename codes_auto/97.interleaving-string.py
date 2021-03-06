#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] interleaving-string
#
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        self.res = False
        @functools.lru_cache(None)
        def helper(last1, last2, last3):
            if not last3:
                self.res = True
                return
            # print(last1, last2, last3)
            if last1 and last1[0] == last3[0]:
                helper(last1[1:], last2, last3[1:])
            if last2 and last2[0] == last3[0]:
                helper(last1, last2[1:], last3[1:])
            return
        helper(s1, s2, s3)
        return self.res
# @lc code=end
#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
from collections import defaultdict
# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        tem = defaultdict(list)
        for i,e in enumerate(s):
            tem[e].append(i)
        for i in tem.values():
            if len(i)==1:
                return i[0]
        return -1
# @lc code=end


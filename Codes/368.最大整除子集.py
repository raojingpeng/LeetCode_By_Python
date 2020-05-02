#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
from typing import List
# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2: return nums
        nums.sort()
        dp = [[i] for i in nums]
        for i in range(1, n):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + [nums[i]], key=len)
                    # print(dp)
        return max(dp,key=len)
# @lc code=end
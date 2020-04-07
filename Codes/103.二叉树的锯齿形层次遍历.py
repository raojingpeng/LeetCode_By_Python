#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        def helper(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            if depth % 2 != 0: # 偶数层
                res[depth].insert(0, root.val)
            else: # 奇数层
                res[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        
        helper(root, 0)
        return res
# @lc code=end


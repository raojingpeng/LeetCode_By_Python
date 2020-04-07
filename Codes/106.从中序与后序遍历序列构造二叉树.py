#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        tem_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:tem_index], postorder[:tem_index])
        root.right = self.buildTree(inorder[tem_index + 1:], postorder[tem_index:-1])
        
        return root
# @lc code=end


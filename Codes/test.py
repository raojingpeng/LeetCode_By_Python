#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
from collections import Counter
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ls = []
        p = head
        # 先将所有结点值扫描进列表
        while p:
            ls.append(p.val)
            p = p.next
        # 利用Counter进行计数
        nums_dict = Counter(ls)
        H = ListNode(-1)
        p = H
        # 将所有value值为1的重新建立结点
        for i in nums_dict.keys():
            if nums_dict[i] == 1:
                p.next = ListNode(i)
                p = p.next
        return H.next
# @lc code=end

if __name__ == "__main__":
    s = "abc d"
    s.replace(" ", "%20")
    print(s)

[1, 1, 1],
[1, 1, 0],
[1, 0, 1]

[2, 2, 2],
[2, 2, 0],
[2, 0, 1]


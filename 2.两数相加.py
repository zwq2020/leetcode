#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = l1 if length(l1) >= length(l2) else l2
        p2 = l2 if length(l1) >= length(l2) else l1
        flag = 0
        while p1:
            p1.val = (p1.val if p1 else 0) + (p2.val if p2 else 0) + flag
            flag = p1.val // 10
            p1.val %= 10
            if not p1.next and flag:
                p1.next = ListNode(0)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return l1 if length(l1) >= length(l2) else l2

# @lc code=end


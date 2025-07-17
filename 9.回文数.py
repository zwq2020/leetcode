#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xnew = list()
        if x < 0:
            return False
        while x:
            xnew.append(x % 10)
            x //= 10
        return xnew == xnew[::-1]
# @lc code=end


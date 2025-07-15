#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = list()
        for ch in s:
            if ch in map.keys():
                if not stack or stack[-1] != map[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
# @lc code=end


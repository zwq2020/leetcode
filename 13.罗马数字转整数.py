#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        ans = 0
        for i,data in enumerate(s):
            if i < n - 1 and dic[data] < dic[s[i + 1]]:
                ans = ans - dic[data]
            else:
                ans = ans + dic[data]
        return ans

# @lc code=end


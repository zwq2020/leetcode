#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                    break
                else:
                    if j == len(needle) - 1:
                        return i
        return -1
# @lc code=end


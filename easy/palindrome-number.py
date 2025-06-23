#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x) :
        if x < 0:
            return False
        return str(x) == str(x)[::-1]   #intをstrにかえて逆にしてもとのと比べてる


a=Solution()
print(a.isPalindrome(10))
b=123456
print(type(str(b)))
print(str(b)[0:3:-1])
print(str(b)[3:0:-1])   #成功例







        
        
# @lc code=end


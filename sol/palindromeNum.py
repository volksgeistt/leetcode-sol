class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        if x % 10 == 0 and x != 0:
            return False
            
        reversed_num = 0
        original = x
        
        while x > 0:
            digit = x % 10 
            reversed_num = (reversed_num * 10) + digit  
            x //= 10  
            
        return original == reversed_num
    
# https://leetcode.com/problems/palindrome-number

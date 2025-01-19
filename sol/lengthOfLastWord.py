class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        l = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            l += 1
        return l
    
# https://leetcode.com/problems/length-of-last-word

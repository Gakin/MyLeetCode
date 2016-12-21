#Solution directly taken from https://discuss.leetcode.com/topic/17110/my-straightforward-python-solution
class Solution(object):
    #I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        sum = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                sum -= roman[s[i]]
            else:
                sum += roman[s[i]]
        return sum + roman[s[-1]]

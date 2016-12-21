class Solution(object):
    def longestPalindrome(self, s):
        length = 0
        dict = {}
        extra = False
        for i in s:
            try:
                dict[i] += 1
            except:
                dict[i] = 1
        for key in dict:
            if dict[key] % 2 == 0:
                length += dict[key]
            elif dict[key] / 2 > 0:
                length += (dict[key] / 2)*2
                extra = True
            else:
                extra = True
        if extra:
            return length + 1
        else:
            return length 

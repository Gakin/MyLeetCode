class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        if len(s) != len(t):
            return False
        for i in s:
            try:
                dict[i] += 1
            except:
                dict[i] = 1
        for i in t:
            try:
                if dict[i] > 0:
                    dict[i] -= 1
                else:
                    return False
            except:
                return False
        return True

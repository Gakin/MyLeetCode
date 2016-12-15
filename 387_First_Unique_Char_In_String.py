class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        resultIndex = 0
        dict = {}
        for i in s:
            try:
                dict[i] += 1
            except:
                dict[i] = 1
        for i in s:
            if dict[i] == 1:
                return resultIndex
            else:
                resultIndex += 1
        return -1

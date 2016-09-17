class Solution(object):
    def canWinNim(self, n):
        if n < 4:
            return True
        if n%4 is 0:
            return False
        else:
            return True

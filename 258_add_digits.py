class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        #Algorithm is called digital root
        return num - 9*((num-1)/9)

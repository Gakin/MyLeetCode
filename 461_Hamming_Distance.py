class Solution(object):
    def hammingDistance(self, x, y):
        mylist = x ^ y
        hammdist = 0
        bindigits = list(bin(mylist))
        for i in range(2,len(bindigits)):
            if bindigits[i] == '1':
                hammdist += 1
        return hammdist    

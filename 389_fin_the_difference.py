class Solution(object):
    def findTheDifference(self, s, t):
        hash = {}
        for char in s:
            try:
                hash[char]
                hash[char] += 1
            except:
                hash[char] = 1
        for char in t:
            try:
                hash[char]
                if hash[char] is 0:
                    return char
                else:
                    hash[char] -= 1
            except KeyError:
                return char

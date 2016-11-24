class Solution(object):
    def findContentChildren(self, g, s):
        result = 0
        g.sort()
        s.sort()
        gIndex = 0
        sIndex = 0
        if len(s) == 0 or len(g) == 0:
            return 0
        while gIndex < len(g) and sIndex < len(s):
            #print str(g[gIndex]) + " : " + str([sIndex])
            if g[gIndex] <= s[sIndex]:
                result += 1
                sIndex += 1
                gIndex += 1
            else:
                sIndex += 1
        return result

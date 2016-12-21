class Solution(object):
    def intersect(self, nums1, nums2):
        dict = {}
        result = []
        for i in nums1:
            try:
                dict[i] += 1
            except:
                dict[i] = 1
        for i in nums2:
            try:
                if dict[i] > 0:
                    result.append(i)
                    dict[i] -= 1
            except:
                continue
        return result

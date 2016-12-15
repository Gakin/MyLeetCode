class Solution(object):
    def intersection(self, nums1, nums2):
        dict1 = {}
        dict2 = {}
        resultList = []
        for i in nums1:
            try:
                dict1[i]
            except:
                dict1[i] = 1
        for i in nums2:
            try:
                if dict1[i] == 1:
                    dict1[i] -= 1
                    resultList.append(i)
            except:
                continue
        return resultList

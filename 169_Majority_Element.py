class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        condition = len(nums)/2
        dict = {}
        for i in nums:
            try:
                dict[i] += 1
            except:
                dict[i] = 1
        for key in dict:
            if dict[key] > condition:
                return key
            else:
                continue

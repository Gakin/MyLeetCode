class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for i in nums:
            try:
                dict[i]
                return True
            except:
                dict[i] = 0
        return False

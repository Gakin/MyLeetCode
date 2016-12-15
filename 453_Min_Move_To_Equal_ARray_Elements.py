class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Credits to https://discuss.leetcode.com/user/rbtchc
        #Original Solution https://discuss.leetcode.com/topic/67054/simple-o-n-python-solution

        min_val = min(nums)
        return sum([v-min_val for v in nums])

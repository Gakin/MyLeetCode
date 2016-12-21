#Negation algorithm is used
#The index of the numbers that are not negated are the numbers that are missing from the list
class Solution(object):
    def findDisappearedNumbers(self, nums):
        sortBool = True
        index = 0
        result = []
        for i in range(0,len(nums)):
            val = abs(nums[i])-1
            if nums[val]>0:
                nums[val]= -nums[val] 
        for i in range(0,len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result

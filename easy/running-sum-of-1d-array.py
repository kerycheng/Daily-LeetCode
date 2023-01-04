class Solution(object):
    def runningSum(self, nums):
        new_sums = []
        current_nums = 0
        for i in range(len(nums)):
            current_nums += nums[i]
            new_sums.append(current_nums)
            
        return new_sums
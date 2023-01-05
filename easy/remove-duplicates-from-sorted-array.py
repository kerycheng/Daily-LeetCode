class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[head] = nums[i]
                head += 1
        return head
# PROBLEM DESCRIPTION:
# Given an array nums, write a function to move all 0's to the end of it while maintaining the
# relative order of the non-zero elements.
# 
# EXAMPLE:
# 
# INPUT:                                OUTPUT: 
# [0,1,0,3,12]                          [1,3,12,0,0]
# 
# NOTE:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0,1,0,3,12]
        if len(nums) < 2:
            return 
        
        i, j = 0, 0
        while j < len(nums):
            while i < len(nums) and nums[i]:
                i += 1
            print("i:", i)
            if i>j: j = i+1
            while j < len(nums) and not nums[j]:
                j += 1
            if i < len(nums) and j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
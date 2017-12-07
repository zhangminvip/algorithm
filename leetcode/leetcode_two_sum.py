# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:00:37 2017

@author: zhangmin
"""



class Solution:
    '''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:
	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
    
    
    '''
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0
        
        while (i < len(nums)):
            j = i + 1
            while (j < len(nums)):
                if(nums[j] == target - nums[i]):
                    return [i,j]
                j += 1
            i += 1
            
S = Solution()
nums = [3,3]
print(S.twoSum(nums,6))
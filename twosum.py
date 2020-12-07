# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
nums = [3, 14, 7, 55, 88, 6]
target = 9

class Solution:
    def twoSum(self, nums, target):
        output = {}
        for index, value in enumerate(nums):
            if value in output:
                return [output[value], index]
            output[target - value] = index
            

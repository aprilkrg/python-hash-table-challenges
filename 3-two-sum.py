'''
https://leetcode.com/problems/two-sum/
3. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''    

def two_sum(nums, target):
  # === ! naive, loop based solution ! === #
  table = {}
  # loop over the number set
    # loop over number set to compare every item to every other item
    # skip loop if both loops are at the same index
    # add the numbers and see if they match the target
  pass

two_sum([3,3], 6)
two_sum([3,2,4], 6)
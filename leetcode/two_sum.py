'''https://leetcode.com/problems/two-sum/'''

class Solution:
    '''https://leetcode.com/problems/two-sum/'''
    def twoSum(self, nums: list(), target: int) -> list():
        for index,num in enumerate(nums):
            next_num = target - num
            if next_num in nums[index+1:]:
                next_index = nums.index(next_num,index+1,)
                return [index,next_index]
            else:
                continue




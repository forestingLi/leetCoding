class Solution:
    def minSubArrayLen(self, s, nums):
        left = 0
        right = -1
        max_index = len(nums)
        sum = 0
        res = max_index + 1

        while(left< max_index):
            if(sum < s and right < max_index -1):
                right += 1
                sum += nums[right]
            else:
                sum -= nums[left]
                left += 1

            if(sum >= s):
                res = min(res,right-left+1)
        if(res == max_index + 1):
            res = 0

        return res








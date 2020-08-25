class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums)
        #数组为空，直接返回-1
        if (length == 0):
            return -1

        left = 0
        right = length - 1

        while(left < right):
            # mid 取左中位数
            mid = int(left + (right-left)/2)
            if(nums[mid] == target):
                return mid
            #排除中位数。这里是左中位数，所以写排除左中位数的分支
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid

        # 需要单独判定最后一个数是否满足条件
        if (nums[mid] == target):
            return mid
        else:
            return -1


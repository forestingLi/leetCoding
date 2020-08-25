class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while(left < right):
            # mid 取左中间数
            mid = left + (right - left)//2
            # 中间数比右边界值大，排除中间数以左的数（包含中间数）
            # mid 要排除左中间数
            if(nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid
        return nums[left]






# 有重复的数字
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while(left < right):
            mid = left + (right - left)//2
            if(nums[mid] > nums[right]):
                left = mid + 1
            elif(nums[mid] < nums[right]):
                right = mid
            # 中间数 等于有边界时，将有边界左移一位
            # 去掉有边界，中间数还在，不影响结果
            else:
                right -= 1

        return nums[left]
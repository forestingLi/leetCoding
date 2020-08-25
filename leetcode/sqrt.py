class Solution:
    def mySqrt(self, x: int) -> int:
        #为了包含0
        left = 0

        #为了包含1
        right = x//2 + 1

        while(left < right):
            #根据if的第一个分支，这里应该取右中位数
            mid = left + (right - left + 1)//2
            # mid * mid > x, mid 肯定不是需要寻找的值，所以，首先排除。
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        # 因为所要搜寻的值肯定在其中，所以，无需进一步判断。
        return left
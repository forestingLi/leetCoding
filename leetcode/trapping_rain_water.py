''' https://leetcode.com/problems/trapping-rain-water/ '''
class Solution:
    def trap(self, height: List[int]) -> int:
        warter = 0
        if len(height) <= 2:
            return warter
        left_index = 0
        right_index = len(height) - 1
        left_max = right_max = 0
        while(left_index < right_index):
            if(height[left_index] < height[right_index]):
                if(height[left_index] < left_max):
                    warter += (left_max - height[left_index])
                else:
                    left_max = height[left_index]
                
                left_index += 1
            else:
                if(height[right_index] < right_max):
                    warter += (right_max - height[right_index])
                else:
                    right_max = height[right_index]
                
                right_index -= 1
                    
        return warter

        

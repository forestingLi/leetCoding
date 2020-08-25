'''https://leetcode.com/problems/zigzag-conversion/'''
class Solution:
    def convert(self, s: str,numRows: int) -> str:
        if (numRows == 1 or numRows >= len(s)):
            return s
    
            ''' Example:
            input :a b c d e f g h i j k
            numRows = 3
            
                    a   e   i
                    b d f h j
                    c   g   k

                    a b c d e f g h i j k
     
            line index: 0 1 2 1 0 1 2 1 0 1 2'''
        zig_zag_list = ["" for i in range(numRows)]
        line_index,step = 0,1
        for char in s:
            zig_zag_list[line_index] += char
            line_index += step
            if (step == 1 and line_index == numRows - 1):
                step = -1
            if(step == -1 and line_index == 0):
                step = 1
        new_str = "".join(zig_zag_list)
        return new_str

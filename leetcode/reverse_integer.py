class Solution:
    def reverse(self, x: int) -> int:
        int2string = str(x)
        new_str = str()
        new_num = 0
        if int2string[0] == "-":
            new_str = int2string[0]
        str_length = len(int2string)
        for index in range(str_length-1,-1,-1):
            if(int2string[index] == '0'and (new_str == "" or new_str == "-")):
                continue
            if (int2string[index] != "-"):
                new_str += int2string[index]
        if new_str:
            new_num = int(new_str)
        if new_num > 2**31 -1 or new_num < - 2**31:
            return 0
        else:
            return new_num
        

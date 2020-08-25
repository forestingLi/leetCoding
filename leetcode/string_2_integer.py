class Solution:
    def my_atoi(self, str: str) -> int:
        result_num = 0
        if not str:
            return result_num
        str = str.strip()
        new_str = str()
        for index in range(len(str)):
            if index == 0 and (str[index] == '-' or str[index] == '+'):
                new_str = str[index]

            if str[index].isspace() and new_str == "":
                continue
            elif str[index].isspace() and new_str:
                break

            if str[index].isdigit():
                new_str += str[index]
            
            else:
                break
        if new_str and new_str != "-" and new_str != "+":
            result_num = int(new_str)
        if result_num > 2**31 - 1 :
            result_num = 2**31 - 1
        elif result_num < -2**31:
            result_num = -2**31
        return result_num
            

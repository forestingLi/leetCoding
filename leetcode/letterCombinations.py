class Solution:
    def letterCombinations(digits: str):
        num2alpha = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        str_list = list()
        if not digits:
            return str_list
        for each_digit in digits:
            if not str_list:
                for each_alpha in num2alpha[each_digit]:
                    str_list.append(each_alpha)
            else:
                str_lenght = len(str_list)
                origin_str = str_list
                str_list = list()
                for i in range(str_lenght):
                    new_str = list()
                    for each_alpha in num2alpha[each_digit]:
                        new_str.append(origin_str[i]+each_alpha)
                    str_list.extend(new_str)
        return str_list

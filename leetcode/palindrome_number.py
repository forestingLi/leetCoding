class Solution:
    def isPalindrome(self, x: int) -> bool:
        int2string = str(x)
        is_palindrome = True
        str_length = len(int2string)
        for index in range(int(str_length/2)):
            if int2string[index] == int2string[str_length-1-index]:
                continue
            else:
                is_palindrome = False
        return is_palindrome

        

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return
        string_length = len(s)
        char_list = list(s)
        longest_palindrome = str()
        for pre_index in range(string_length):
            char_start_index = pre_index
            for post_index in range(string_length-1,1,-1):
                char_end_index = post_index
                while (char_list[pre_index] == char_list[post_index] and pre_index < post_index - 1):
                    pre_index = pre_index + 1
                    post_index = post_index - 1
                    if pre_index == post_index or pre_index == post_index - 1:
                        palindrome = str(char_list[char_start_index:char_end_index])
                        break
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
        if longest_palindrome:
            return longest_palindrome
        else:
            return





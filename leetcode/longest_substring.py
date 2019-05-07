'''https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/'''

class Solution:
    def lengthOfLongestSubstring(self, s: str, retrun=None) -> int:
        length_of_sub_str = 0
        if s is None:
            return length_of_sub_str

        sub_str = str()
        current_length = 0
        for char in s:
            if char not in sub_str:
                current_length += 1
                sub_str += char
            else:
                length_of_sub_str =max(length_of_sub_str, len(sub_str))
                char_index = sub_str.index(char)
                sub_str_right = sub_str[char_index+1:]
                sub_str = sub_str_right + char
                current_length = len(sub_str)
        length_of_sub_str = max(current_length,length_of_sub_str)
        return length_of_sub_str

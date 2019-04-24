class Solution:
    ''' https://leetcode.com/problems/longest-palindromic-substring/'''
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        string_length = len(s)
        longest_palindrome = str()
        for pre_index in range(string_length):
            char_start_index = pre_index
            for post_index in range(string_length-1,char_start_index,-1):
                pre_index = char_start_index #
                char_end_index = post_index
                # print("### one interation begin with pre index :{}, post index:{}####".format(char_start_index,char_end_index))
                palindrome = str()
                while (s[pre_index] == s[post_index]):
                    # print("pre_index : {} \n".format(pre_index))
                    # print("post_index : {} \n".format(post_index))

                    if(pre_index < post_index -1):
                        pre_index = pre_index + 1
                        post_index = post_index - 1

                    elif ((pre_index == post_index) or ((pre_index == post_index - 1))):
                        palindrome = ''.join(s[char_start_index:char_end_index+1])
                        # print("palindrom: {}\n".format(palindrome))
                        break

                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
        if longest_palindrome:
            return longest_palindrome
        elif s:
            return s[0]


    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindromic_str = ""
        max_len = 0
        for i in range(len(s)):
            start_index = end_index = i
            while(end_index+1 < len(s) and s[end_index] == s[end_index+1]):
             #   print " here while 1"
                end_index += 1
             #   print "1. the start and end are %d,%d"%(start_index,end_index)
            if(end_index+1 == len(s)):
                if(end_index-start_index >= max_len):
                    max_len = end_index - start_index
                #    print " 2. the start and end are %d,%d"%(start_index,end_index)
                    palindromic_str = s[start_index:end_index+1]

            else:
                while((start_index-1) >=0 and end_index+1 < len(s) and s[start_index-1] == s[end_index+1]):
              #      print " here while 2"
               #     print "3.the start and end are %d,%d"%(start_index,end_index)
                    start_index -= 1
                    end_index   += 1
                if(end_index-start_index >= max_len):
             #       print "4.the start and end are %d,%d"%(start_index,end_index)
                    max_len = end_index - start_index
                    palindromic_str = s[start_index:end_index+1]
            #print("%d:%d:%d%s"%(i,start_index,end_index,palindromic_str))
        if(palindromic_str == ""):
            palindromic_str = s[0]
        return palindromic_str






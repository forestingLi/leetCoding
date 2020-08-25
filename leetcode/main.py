from leetcode.min_sub_array import Solution

class self:
    if __name__ == '__main__':
        #
        # nums = [1,5,3,4]
        #
        # list = [[1,1,6],[1,7],[2,6]]
        # new_list = [1,2,3,4,5,6]
        # print(new_list[3:5])
        # if new_list not in list:
        #     list.append(new_list)
        #     print("yes")
        # else:
        #     print("No")
        # for i in range(len(nums)):
        #     nums[i] = min(nums[i:])
        # print(nums)

        # str_list = ["" for x in range(3)]
        # print(str_list)
        # next
        # int_str = 0
        # test_string = "-"
        # if test_string and (test_string != "-" or test_string != "+"):
        #     int_str = int(test_string)
        # print(int_str)
        # if test_string[0].isdigit():
        #     print("Yes")
        # for char in range(a,z):

        # string_lenth = len(test_string)
        # print(test_string)
        # char_list = list(test_string)
        # for i in range(3,0,-1):
        #     i = i + 1
        #     print(i)
        #     print("\n")
        # print(char_list[0:string_lenth])
        s = Solution()
        result = s.minSubArrayLen(7,[2,3,1,2,4,3])
        print(result)

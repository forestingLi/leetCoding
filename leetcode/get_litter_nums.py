
# 该方法最直接，但是时间复杂度为O(n^2),效率较低。
def get_smaller_nums1(nums):

    # counts 为该函数的返回列表。
    counts = list()
    nums_length = len(nums)

    # 当输入的数组nums为空时，返回数组也为空。
    if(nums_length == 0):
        return counts

    # for循环实现对数组nums的元素遍历。
    # while循环则实现对当前元素的右侧元素进行遍历，
    # 并记录小于当前元素值的个数。
    # 时间复杂度为O(n²)。
    for index in range(nums_length):
        temp_index = index + 1
        smaller_num_count = 0

        while(temp_index < nums_length):
            if(nums[temp_index] < nums[index]):
                smaller_num_count += 1
            temp_index += 1

        counts.append(smaller_num_count)
    return counts


# 该方法是在方法以的基础上进行了优化。
# 时间复杂度为O(n*logn)
def get_smaller_nums2(nums):

    # counts 为该函数的返回列表。
    counts = list()
    nums_length = len(nums)

    # 当输入的数组nums为空时，返回数组也为空。
    if(nums_length == 0):
        return counts

    # 对数组nums进行逆序遍历，
    # 并将当前元素右侧所有元素进行升序排序，
    # 利用二分查找，查找已排序元素中小于当前所遍历的元素的个数。
    # 时间复杂度为O(n*logn)
    index = nums_length - 1
    temp_nums = list()
    while(index >= 0 ):
        left = 0
        right = len(temp_nums)
        while(left < right):
            # mid 取左中位数
            mid = left + (right - left)//2
            if(nums[index] <= temp_nums[mid]):
                right = mid
            else:
                # left就要将mid进行排除（因为 mid 取左中位数）
                left = mid + 1

        # right 的值，即为已排序数组temp_nums中小于当前元素的数字个数
        # 由于是逆序查找，需要将该结果插入到counts的头部。
        counts.insert(0,right)

        # 查找完毕，将当前元素插入到排序素组中相应位置，以保存数组依然保持升序。
        temp_nums.insert(right,nums[index])
        index -= 1
    return counts

if __name__ == "__main__":
    test_list =[
        [5,2,6,1],
        [3,2,8,9,1,5,3,4],
        [1,2,3,4,5,6,7,8,9],
        [9,8,7,6,5,4,3,2,1],
        [0,0,0,0,0,0,0],
        [1,0,-1,1,-1,1,-1,0,-2,-3],
    ]

    map = dict()
    map['a'] = 'a'
    map['b'] = 'c'

    c = 'c'

    if c in map:
        print("Yes!")

    #
    # for nums in test_list:
    #     result = get_smaller_nums1(nums)
    #     print("The input nums is:{}\nThe output nums : {}\n".format(nums,result))



#定义递归函数hanio_tower_problem（）
#其参数及位置分别表示圆盘所在圆柱及移动轨迹：initial_tower --> temp_tower --> dest_tower
def hanio_tower_problem(initial_tower,temp_tower,dest_tower):
    global nums_4next_move

    #当初始列表的圆盘数目为0的时候，递归结束。
    length = len(initial_tower)
    if (length == 0):
        return

    # 1. 将原始柱上的上面n-1个圆盘当作一个整体进行移动到中转柱上
    # 其移动过程轨迹是initial_tower --> dest_tower --> temp_tower,
    # nums_4next_move用来存储后续需要移动的圆盘。
    nums_4next_move.insert(0,initial_tower[length-1])
    hanio_tower_problem(initial_tower[:length-1],temp_tower,dest_tower)


    # 2. 将initial_tower中后续需要移动的圆盘直接移动到目的圆柱dest_tower中
    num_to_move = nums_4next_move[0]
    nums_4next_move.remove(num_to_move)
    initial_tower = nums_4next_move
    dest_tower = move_num(num_to_move,dest_tower)

    # 3. 再将第1步中，已转移到中转圆柱（temp_tower）上的n-1个圆盘，（经由原始圆柱）移动到目的圆柱dest_tower.
    hanio_tower_problem(temp_tower,initial_tower,dest_tower)

def move_num(num,dest_list):
    print("Moving {} to destional number list. ".format(num))
    #将圆盘放置在圆柱的顶部（不能从底部放入）
    # num = nums.pop()
    # nums.remove(num)
    dest_list.append(num)
    print("The dest tower is {}. \n".format(dest_list))
    # if(len(nums)==0):
    #     print("Game over, Successed!")
    return dest_list


if __name__ == "__main__":

    #定义一个初始列表initial_nums，表示原始柱子上n个圆盘的堆叠顺序。
    #其中，其数字的index从0 --> n-1 的位置对应圆柱从上到下的圆盘位置。
    # Example: [0,1,2,3]表示圆柱从上到下的圆盘为0，1，2，3
    n = 8
    initial_nums = [x for x in range(n)]

    # 定义一个全局的列表，用来存储后续需要移动的圆盘
    nums_4next_move = list()

    #temp_nums 为中转圆柱,dest_nums为目的地圆柱。
    temp_nums = list()
    dest_nums = list()
    hanio_tower_problem(initial_nums,temp_nums,dest_nums)



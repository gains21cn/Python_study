# 选择排序
#
# The algorithm works by selecting the smallest unsorted item
# and then swapping it with the item in the next position to be filled.
#
# The selection sort works as follows:
# you look through the entire array for the smallest element,
# once you find it you swap it (the smallest element) with the first element of the array.
# Then you look for the smallest element in the remaining array (an array without the first element)
# and swap it with the second element.
# Then you look for the smallest element in the remaining array
# (an array without first and second elements) and swap it with the third element,
# and so on. Here is an example,




data_set = [9, 1, 22, 31, 45, 3, 6, 2, 11]

smallest_num_index = 0  # 初始列表最小值,默认为第一个

loop_count = 0
for j in range(len(data_set)):
    for i in range(j, len(data_set)):
        if data_set[i] < data_set[smallest_num_index]:  # 当前值 比之前选出来的最小值 还要小,那就把它换成最小值
            smallest_num_index = i
        loop_count += 1
    else:
        print("smallest num is ", data_set[smallest_num_index])
        tmp = data_set[smallest_num_index]
        data_set[smallest_num_index] = data_set[j]
        data_set[j] = tmp

    print(data_set)
    print("loop times", loop_count)
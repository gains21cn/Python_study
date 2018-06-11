#creat with :PyCharm
#Author:Wilson
#Date:2018/5/3
#Time:14:44

# 快速排序（quick sort）
# 设要排序的数组是A[0]……A[N-1]，首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，
# 然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。
# 值得注意的是，快速排序不是一种稳定的排序算法，也就是说，多个相同的值的相对位置也许会在算法结束时产生变动　　
#
# 注：在待排序的文件中，若存在多个关键字相同的记录，经过排序后这些具有相同关键字的记录之间的相对次序保持不变，
# 该排序方法是稳定的；若具有相同关键字的记录之间的相对次序发生改变，则称这种排序方法是不稳定的。
# 要注意的是，排序算法的稳定性是针对所有输入实例而言的。
# 即在所有可能的输入实例中，只要有一个实例使得算法不满足稳定性要求，则该排序算法就是不稳定的。
#
#排序演示
# 示例
# 假设用户输入了如下数组：
# 下标            0   1   2   3   4   5
# 数据627389
# 创建变量i=0（指向第一个数据）, j=5(指向最后一个数据), k=6(赋值为第一个数据的值)。
# 我们要把所有比k小的数移动到k的左面，所以我们可以开始寻找比6小的数，
# 从j开始，从右往左找，不断递减变量j的值，
# 我们找到第一个下标3的数据比6小，于是把数据3移到下标0的位置，
# 把下标0的数据6移到下标3，完成第一次比较：
#
# 下标            0   1   2   3   4   5
# 数据            3   2   7   6   8   9
# i=0 j=3 k=6
#
# 接着，开始第二次比较，这次要变成找比k大的了，而且要从前往后找了。
# 递加变量i，发现下标2的数据是第一个比k大的，
# 于是用下标2的数据7和j指向的下标3的数据的6做交换，数据状态变成下表：
# 下标            0   1   2   3   4   5
# 数据            3   2   6   7   8   9
# i=2 j=3 k=6
# 称上面两次比较为一个循环。
#
# 接着，再递减变量j，不断重复进行上面的循环比较。
# 在本例中，我们进行一次循环，就发现i和j“碰头”了：他们都指向了下标2。
# 于是，第一遍比较结束。得到结果如下，凡是k(=6)左边的数都比它小，凡是k右边的数都比它大：
# 下标            0   1   2   3   4   5
# 数据            3   2   6   7   8   9
#
# 如果i和j没有碰头的话，就递加i找大的，还没有，就再递减j找小的，如此反复，不断循环。
# 注意判断和寻找是同时进行的。
#
# 然后，对k两边的数据，再分组分别进行上述的过程，直到不能再分组为止。
# 注意：第一遍快速排序不会直接得到最终结果，只会把比k大和比k小的数分到k的两边。
# 为了得到最后结果，需要再次对下标2两边的数组分别执行此步骤，然后再分解数组，
# 直到数组不能再分解为止（只有一个数据），才能得到正确结果。

# _*_coding:utf-8_*_
__author__ = 'Alex Li'


def quick_sort(array, left, right):
    '''

    :param array:
    :param left: 列表的第一个索引
    :param right: 列表最后一个元素的索引
    :return:
    '''
    if left >= right:
        return
    low = left
    high = right
    key = array[low]  # 第一个值

    while low < high:  # 只要左右未遇见
        while low < high and array[high] > key:  # 找到列表右边比key大的值 为止
            high -= 1
        # 此时直接 把key(array[low]) 跟 比它大的array[high]进行交换
        array[low] = array[high]
        array[high] = key

        while low < high and array[low] <= key:  # 找到key左边比key大的值，这里为何是<=而不是<呢？你要思考。。。
            low += 1
            # array[low] =
        # 找到了左边比k大的值 ,把array[high](此时应该刚存成了key) 跟这个比key大的array[low]进行调换
        array[high] = array[low]
        array[low] = key

    quick_sort(array, left, low - 1)  # 最后用同样的方式对分出来的左边的小组进行同上的做法
    quick_sort(array, low + 1, right)  # 用同样的方式对分出来的右边的小组进行同上的做法


if __name__ == '__main__':
    array = [96, 14, 10, 9, 6, 99, 16, 5, 1, 3, 2, 4, 1, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3, 22, 19, 2]
    # array = [8,4,1, 14, 6, 2, 3, 9,5, 13, 7,1, 8,10, 12]
    print("before sort:", array)
    quick_sort(array, 0, len(array) - 1)

    print("-------final -------")
    print(array)
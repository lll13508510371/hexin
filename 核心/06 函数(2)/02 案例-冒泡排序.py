"""
    需求: 任意给定一组序列数字,
    比如 [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48],
    将序列从小到大排列。（不能使用python函数解决）
"""


def Bubble_Sort(arr):  # 这个参数后续必须传一个序列 --> 列表

    n = len(arr)  # 计算序列的长度, 后续用于循环推导比大小的轮次

    # [46, 4, 19, 50, 48]  012345
    for i in range(n):  # 遍历序列长度的索引, 比较的轮次
        for j in range(0, n - 1):  # 构建序列索引的循环, 取不到最后一个数字 0123
            if arr[j] > arr[j + 1]:  # 如果取出来的第一个数大于第二个数
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(Bubble_Sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))
print(Bubble_Sort([45, 13, 64, 36, 58, 2, 5, 1, 79]))

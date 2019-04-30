#最大连续子数组
#输入一个整形数组，数组里有正数也有负数。数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。 求所有子数组的和的最大值，要求时间复杂度为O(n)。
#例如输入的数组为1, -2, 3, 10, -4, 7, 2, -5，和最大的子数组为3, 10, -4, 7, 2， 因此输出为该子数组的和18。

# 解法：
# 事实上，当我们令currSum为当前最大子数组的和，maxSum为最后要返回的最大子数组的和，当我们往后扫描时，
# 对第j+1个元素有两种选择：要么放入前面找到的子数组，要么做为新子数组的第一个元素；
# 如果currSum加上当前元素a[j]后不小于a[j]，则令currSum加上a[j]，否则currSum重新赋值，置为下一个元素，即currSum = a[j]。
# 同时，当currSum > maxSum，则更新maxSum = currSum，否则保持原值，不更新。

def MaxSubArray(arr):
    if len(arr) == 0:
        return 0
    max_sum, cur_sum = 0, 0
    for i in range(0, len(arr)):
        #新加入的值只要是正向影响我们就加入进去
        if cur_sum + arr[i] >= arr[i]:
            cur_sum += arr[i]
        else:
            cur_sum = arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
        #print(cur_sum, max_sum)
    return max_sum

arr=[1, -2, 3, 10, -4, 7, 2, -5, 90]
print(MaxSubArray(arr))
#旋转数组查找默认升序

# 思路：旋转数组取中间位置至少有一边是有序的，利用有序快速判断key在那一边,有序的
#      部分可以快速用二分查找定位
def Search(arr, key):
    if len(arr) == 0:
        return -1
    
    beg, end = 0, len(arr) - 1
    while beg <= end:
        mid = (beg + end) // 2
        cur = arr[mid]

        if cur == key:
            return cur
        #默认升序，左边有序
        if cur > arr[beg]:
            if cur > key and key >= arr[beg]: #确实key在左边区间
                end = mid - 1
            else:
                beg = mid + 1
        #右边有序
        if cur < arr[end]:
            if cur < key and key <= arr[end]: #确实key在右边区间
                beg = mid + 1
            else:
                end = mid - 1
        #print('--------------', arr[beg], arr[end])
    return -1

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(Search(arr, 25))
print(Search(arr, 15))
print(Search(arr, 1))
print(Search(arr, 14))
print(Search(arr, 5))
print(Search(arr, 26))

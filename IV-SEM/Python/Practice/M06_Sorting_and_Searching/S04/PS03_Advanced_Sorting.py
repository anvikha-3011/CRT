def Partition(arr,low,high):
    pivot = arr[low]
    i, j = low + 1,high 
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

def QuickSort(arr,low,high):
    if low < high:
        pi = Partition(arr,low,high)
        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)
    return arr
print(QuickSort([54,26,98,17,77,31,44,55,20],0,8))

#leetcode 912. Sort an Array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return QuickSort(nums,0,len(nums)-1)
    

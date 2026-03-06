import random
nums = [6, 9, 7, 12, 1, 11, 5, 2]
def merge(arr:int,low:int,mid:int,high:int):
    final = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            final.append(arr[left])
            left += 1
        else:
            final.append(arr[right])
            right += 1
    while left <= mid:
            final.append(arr[left])
            left+=1
    while right <= high:
            final.append(arr[right])
            right += 1
    for i in range(low, high + 1):
        arr[i] = final[i - low]
def mergeSort(arr:list,low:int,high:int):
    if low == high:
        return
    mid = (low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)
mergeSort(nums,0,len(nums)-1)
print(nums)

"""recursive bubble sort"""
# nums = [6, 9, 7, 12, 1, 11, 5, 2]
# def bubbleSort(arr:list,n:int):
    # if n == 1:
    #     return
    # counter = 0
    # for j in range(n-1):
    #     if arr[j+1] < arr[j]:
    #         temp = arr[j+1]
    #         arr[j+1] = arr[j]
    #         arr[j] = temp
    #         counter = 1
    # if counter == 0:
    #     return
    # bubbleSort(arr,n-1)
# bubbleSort(nums,len(nums))
# print(nums)

"""Recursive insertion sort"""
# def insertionSort(arr:list,n:int=1) -> None:
#     if n >= len(nums):
#         return
#     j = n
#     while j-1 >= 0 and j <= len(arr):
#         if arr[j-1] > arr[j]:
#             temp =  arr[j]
#             arr[j] = arr[j-1]
#             arr[j-1] = temp
#         j -=1
#     insertionSort(arr,n+1) 
# insertionSort(nums,1)
# print(nums)
"""Quick Sort Algorithm"""
# print("Running Quick Sorting")
# nums = [6, 4, 2, 7, 5, 3, 1]

# def partition(arr,low,high):
#     i = low
#     j = high
#     pivot = arr[low]
#     while j > i:
#         while arr[i] <= pivot and i < high:
#             i += 1
#         while arr[j] > pivot and j > low:
#             j -= 1
#         if j > i :
#             temp = arr[j]
#             arr[j] = arr[i]
#             arr[i] = temp
#     temp = arr[j]
#     arr[j] = arr[low]
#     arr[low] = temp
#     return j

# def quick_sort(arr,low,high):
    
#     if low >= high:
#         return
#     Pidx = partition(arr,low,high)
#     quick_sort(arr,low,Pidx-1)
#     quick_sort(arr,Pidx+1,high)    
# quick_sort(nums,0,len(nums)-1)
    
    
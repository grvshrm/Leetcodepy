class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        low, high = 0, len(nums) - 1
        self.mergeSort(nums, low, high)
        return nums
    
    def mergeSort(self, arr: [int], low: int, high: int):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid+1, high)
        self.merge(arr, low, mid, high)

    def merge(self, arr: [int], low: int, mid: int, high: int):
        left, right = low, mid+1
        temp = []
        while(left <= mid and right <= high):
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while(left <= mid):
            temp.append(arr[left])
            left += 1
        while(right <= high):
            temp.append(arr[right])
            right += 1
        for i in range(low, high+1):
            arr[i] = temp[i - low]

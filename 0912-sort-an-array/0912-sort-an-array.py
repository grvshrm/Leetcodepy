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

    """def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
        
    def partition(self, arr: list, low: int, high: int):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while i <= high-1 and arr[i] <= pivot:
                i += 1
            while j >= low+1 and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]
        return j

    def quickSort(self, arr: list, low: int, high: int):
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSort(arr, low, pIndex - 1)
            self.quickSort(arr, pIndex + 1, high)"""
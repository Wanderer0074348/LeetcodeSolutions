class QuickSort:
    def sort(self, nums: list[int]):
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums: list[int], low: int, high: int):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quick_sort(nums, low, pi - 1)
            self.quick_sort(nums, pi + 1, high)

    def partition(self, nums: list[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]):
        nums = nums1 + nums2
        QuickSort().sort(nums)
        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2
        return nums[n // 2]


x = Solution()
print(type(x.findMedianSortedArrays([1, 3], [2])))
print(x.findMedianSortedArrays([1, 2], [3, 4]))
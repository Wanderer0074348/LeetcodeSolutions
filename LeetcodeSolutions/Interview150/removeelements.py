class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
        nums = [x for x in nums if x != None]
        return len(nums)

a = Solution()
print(a.removeElement([3,2,2,3], 3)) # 2
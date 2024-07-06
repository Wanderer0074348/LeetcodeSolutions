class Solution:
    def merge(self, nums1: list[int], nums2: list[int],m:int,n:int) -> list[int]:
        # two pointer approach
        i,j = 0,0
        temp_arr = []
        while i != m and j != n:
            if nums1[i] < nums2[j]:
                temp_arr.append(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                temp_arr.append(nums2[j])
                j+=1
            else:
                temp_arr.append(nums1[i])
                temp_arr.append(nums2[j])
                i+=1
                j+=1
        #add all remaining elements
        while i != m:
            temp_arr.append(nums1[i])
            i+=1
        while j != n:
            temp_arr.append(nums2[j])
            j+=1
        
        #final sorted array be in nums1
        for i in range(m+n):
            nums1[i] = temp_arr[i]
        
        return nums1
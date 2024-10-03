class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # put the list of nums2 in the list of nums1
        i = 0
        for x in range(m, m + n):
            nums1[x] = nums2[i]
            i += 1
        
        # for y in range(m + n):
            # print(nums1[y])
            
        nums1.sort()
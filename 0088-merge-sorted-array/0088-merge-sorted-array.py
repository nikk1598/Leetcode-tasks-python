class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return nums1
            
        for x in nums2:
            nums1[m] = x
            m += 1
            for i in range(m-1, 1, -1):
                if nums1[i] < nums1[i-1]:
                    nums1[i], nums1[i-1] = nums1[i-1], nums1[i]
                else:
                    break
                    
            if nums1[1] < nums1[0]:
                 nums1[1], nums1[0] = nums1[0], nums1[1]
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums2) == 0:
            return nums1
        
        if len(nums1) == len(nums2):
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
    
        for i in range(m-1, -1, -1):
            nums1[i], nums1[i+len(nums2)] = nums1[i+len(nums2)], nums1[i]
        
        i = n
        j = 0
        curr_pos = 0

        while (j < len(nums2)) and (i < len(nums1)):
            if nums1[i] < nums2[j]:
                nums1[curr_pos] = nums1[i]
                i += 1
            else:
                nums1[curr_pos] = nums2[j]
                j += 1
            curr_pos += 1
        
        while (j < len(nums2)):
            nums1[curr_pos] = nums2[j]
            j += 1
            curr_pos += 1

        return nums1




           
  

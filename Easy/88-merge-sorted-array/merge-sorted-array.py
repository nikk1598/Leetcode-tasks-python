class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            return

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return


        for i in range(len(nums1)-n-1, -1, -1):
            nums1[i+n] = nums1[i]
     
        i = n
        j = 0
        curr_pos = 0
        while True:
            if i >= len(nums1):
                while j < len(nums2):
                    nums1[curr_pos] = nums2[j]
                    curr_pos += 1
                    j += 1
                break
            if j >= len(nums2):
                break
            if nums1[i] < nums2[j]:
                nums1[curr_pos] = nums1[i]
                i += 1
            else:
                nums1[curr_pos] = nums2[j]
                j += 1
            curr_pos += 1

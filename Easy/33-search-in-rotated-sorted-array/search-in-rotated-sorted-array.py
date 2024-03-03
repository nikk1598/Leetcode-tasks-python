class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while r-l > 0:
            m = (l + r) // 2
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m
        k = l
        print(k)

        if target > nums[-1]:
            l, r = 0, k-1
        else:
            l, r = k, len(nums)-1
        while r-l > 0:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if nums[l] == target:
            return l
        else:
            return -1
    


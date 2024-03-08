class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            else:
                k -= 1
        return k

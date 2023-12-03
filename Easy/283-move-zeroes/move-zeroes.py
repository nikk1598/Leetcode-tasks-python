class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_pointer = 0
        second_pointer = 0
        
        while (second_pointer < len(nums) -1):
            if nums[first_pointer] == 0:
                while (nums[second_pointer] == 0) & (second_pointer < len(nums) -1):
                    second_pointer +=1
                nums[first_pointer], nums[second_pointer] = nums[second_pointer], nums[first_pointer]
                
            if second_pointer - first_pointer <= 1:
                second_pointer += 1
                
            first_pointer += 1
            
        if nums[first_pointer] == 0:
            nums[first_pointer], nums[len(nums)-1] = nums[len(nums)-1], nums[first_pointer]
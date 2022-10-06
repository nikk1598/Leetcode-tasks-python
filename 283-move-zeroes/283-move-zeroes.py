class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 1) or (len(nums) == 0):
            return

        first_pointer = 0
        second_pointer = 1
        
        while(second_pointer < len(nums)-1):
            if nums[first_pointer] == 0:
                while (nums[second_pointer] == 0) and (second_pointer < len(nums)-1):
                    second_pointer += 1
                nums[first_pointer], nums[second_pointer] = nums[second_pointer], nums[first_pointer]

            if (second_pointer - first_pointer == 1) and (second_pointer < len(nums)-1): 
                second_pointer += 1  

            first_pointer += 1
            
        if nums[first_pointer] == 0:
             nums[first_pointer], nums[second_pointer] = nums[second_pointer], nums[first_pointer]
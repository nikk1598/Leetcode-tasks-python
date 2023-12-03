class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first_pointer = 0
        second_pointer = 0
        
        if len(nums) == 0:
            return 0
        
        while(second_pointer < len(nums)):
            if nums[first_pointer] == val:
                while(nums[second_pointer] == val) & (second_pointer < len(nums)-1):
                    second_pointer += 1
                nums[second_pointer], nums[first_pointer] = nums[first_pointer], nums[second_pointer]
            
            if second_pointer - first_pointer == 0:
                second_pointer += 1
                
            first_pointer += 1
            
        i = len(nums) - 1
        
        while (nums[i] == val) & (i > -1):
            i -= 1

        nums = nums[0:i+1]
        return i+1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        
        if digits[pointer] < 9:
            digits[pointer] += 1
            return digits
        
        while (digits[pointer] == 9) & (pointer > 0):
            pointer -= 1
            
        if (digits[pointer] == 9) & (pointer == 0):
            return [1] + [0]*len(digits)
        elif digits[pointer] != 9:
            digits[pointer] += 1
            while pointer < len(digits) - 1:
                pointer += 1
                digits[pointer] = 0
            return digits
        
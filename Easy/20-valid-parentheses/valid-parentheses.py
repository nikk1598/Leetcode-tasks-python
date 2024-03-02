class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']':'[', ')':'(', '}':'{'}
        stack = []
        for square in s:
            if square in pairs.values():
                stack.append(square)
            elif (len(stack) != 0) and (stack[-1] == pairs[square]):
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
            
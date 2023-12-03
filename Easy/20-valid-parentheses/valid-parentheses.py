class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for x in s:
            if x in ['(', '{', '[']:
                stack.append(x)
            elif (x in [')', '}', ']']) & (len(stack) == 0):
                return False
            elif stack[-1] != pairs[x]:
                return False
            else:
                stack.pop(-1)

        if len(stack) == 0:
            return True
        else:
            return False
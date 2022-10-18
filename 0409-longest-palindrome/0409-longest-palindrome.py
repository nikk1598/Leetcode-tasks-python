class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for x in s:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
                
        middle_count = 0
        left_right_count = 0
        
        for x in dic.keys():
            if dic[x] == 1:
                middle_count += 1
            elif dic[x] % 2 == 0:
                left_right_count += dic[x]
            elif (dic[x] % 2) != 0:
                left_right_count += dic[x]-1
                middle_count += 1

        
        if middle_count == 0:
            return left_right_count
        else:
            return left_right_count+1
            
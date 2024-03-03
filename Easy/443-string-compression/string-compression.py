class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append(-1)
        i = 0
        count = 1
        for j in range(1, len(chars)):
            if chars[j] == chars[j-1]:
                count += 1
            else:
                if count == 1:
                    chars[i] = chars[j-1]
                    i += 1
                else:
                    chars[i] = chars[j-1]
                    i += 1
                    count_s = str(count)
                    for k in range(len(count_s)):
                        chars[i] = count_s[k]
                        i += 1
                count = 1
        return i
            





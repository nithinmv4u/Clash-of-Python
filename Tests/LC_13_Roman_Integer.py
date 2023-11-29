from functools import reduce
class Solution(object):
    def romanToInt(self, s):
        numerals = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        prev = 0
        result = 0
        # if 'I' in numerals:print("yes")
        for i in range(len(s)-1, -1, -1):
            print(s[i])
            if s[i] in numerals:
                # print(numerals.get(s[i]))
                if prev > numerals.get(s[i]):
                    result = result - numerals.get(s[i])
                else:result = result + numerals.get(s[i])
                prev = numerals.get(s[i])
            else:result = 0
            print(result, prev)
        return result
    
    #not working
    def romanToInt2(self, s):
        numerals = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        num_list = [numerals.get(x) for x in s]
        print(num_list)
        result = reduce(lambda x, y : x - y if x > y else x + y, num_list[::-1])
        print(result)

# roman = "III"
roman = "LVIII"
# roman = "XCIX"
result = Solution().romanToInt(roman)

print(result) if result > 0 else print("not roman")
result = Solution().romanToInt2(roman)
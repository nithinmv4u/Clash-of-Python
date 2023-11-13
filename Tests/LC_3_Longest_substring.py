class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        new_length = 0
        sub_string = ""
        new_string = ""
        for i in range(len(s)):
            if s[i] not in new_string:
                print("sub:",s[i])
                new_string+=s[i]
                new_length+=1
                print(new_string, new_length)
            else:
                print(new_string, new_length)
                if max_length<new_length: max_length = new_length
                new_string+=s[i]
                new_length+=1
                for j in range(len(new_string)):
                    if s[i] == new_string[j]:
                        new_string = new_string[j+1:]
                        new_length = len(new_string)
                        print(new_string, new_length)
                        break
        return max_length if max_length>new_length else new_length
                

s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = " "
# s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
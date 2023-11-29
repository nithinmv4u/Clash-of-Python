class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        total = 0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if len(strs[j]) > i and strs[0][i] == strs[j][i]:
                    total+=1
                    print(total)
                else:break
            if total == len(strs)-1:
                prefix += strs[0][i]
                print(prefix)
                total = 0
            else:break
        return prefix
        

# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["ab", "a"]
print(Solution().longestCommonPrefix(strs))
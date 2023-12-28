#---------------NOT WORKING--------------#
# def wordCount(s, i=0, count=0):
#     if i < len(s):wordCount(s, i+1)
#     i -= 1
#     print(s[i])
#     if s[i] != ' ':
#         print(count)
#         count += 1
#     elif count > 0 and s[i] == ' ':
#         return count



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, -1, -1):
            if count > 0 and s[i] == ' ':break
            if s[i] == ' ':
                continue
            else:
                count += 1
        return count

# s = "Hello World"
# s = "   fly me   to   the moon  "
s = "    day"
print(Solution().lengthOfLastWord(s))
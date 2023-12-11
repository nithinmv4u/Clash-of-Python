class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j = 0,0
        print(haystack, needle)
        while i < len(haystack):
            if haystack[i] == needle[j]:
                print(i, j)
                if j == len(needle)-1:
                    print("pass",i, j)
                    return i-j
                j += 1
            else:
                i -= j
                j = 0
            i += 1
        return -1

haystack = "sadbutsad"
needle = "sad"
# haystack = "mississippi"
# needle = "issip"
firstOccurance = Solution().strStr(haystack, needle)
print(firstOccurance)
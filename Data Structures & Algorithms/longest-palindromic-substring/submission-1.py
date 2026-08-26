class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxp = ""

        for i in range(len(s)):
            l = r = i

            test = ""

            while l >= 0 and r < len(s) and s[l] == s[r]:
                test = s[l:r+1]
                # print(test)
                l -= 1
                r += 1
            maxp = test if len(test) > len(maxp) else maxp

            l = i
            r = i + 1

            test = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                test = s[l:r+1]
                # print(" ", test)
                l -= 1
                r += 1
            maxp = test if len(test) > len(maxp) else maxp


        return maxp
class Solution:
    def countSubstrings(self, s: str) -> int:
        #we can check the i-1 and i+1 index to see if theyre equal, that means it a palindrome, +1 count
        # then we just repeat until we meet the bounds
        #however this only works for odd palindromes

        #even palindromes we just must check the next element

        #we can recursively call the next cycle of the palindrom ething
        
        res = 0

        #better approach

        for i in range(len(s)):
            l = r = i

            # odd lengths check
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            #even lengths check
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res




    #     for i in range(len(s)):
    #         res += 1 + self.check(s, i-1, i+1) + self.check(s, i, i+1)

    #     return res


    # def check(self, s: str, l: int, r: int) -> int:
    #     if l < 0 or r >= len(s):
    #         return 0

    #     if s[l] == s[r]:
    #         return 1 + self.check(s, l-1, r+1)
    #     return 0


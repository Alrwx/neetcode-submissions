class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #set for the letters
        # sliding window
        # once we find dupe, we pop until its no longer there

        charSet = set()
        L = 0
        count = 0

        for R in range(len(s)):
            # remove until its not there by updating the left pointer 
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            count = max(count, len(charSet))
        return count
                         
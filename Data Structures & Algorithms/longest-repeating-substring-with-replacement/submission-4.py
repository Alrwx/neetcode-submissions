
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # map of the freq of each letter, max size 26
        counts = {}

        #l and right pointers

        max_count = 0
        bigfrq = 0

        l = 0
        r = l

        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r],0)
            length = r - l + 1

            if length - max(counts.values()) <= k:
                # good on replacements
                max_count = max(max_count, length)
            else:
                #incr l until it fits
                c = max(counts.values())
                while (r-l+1) - c > k:
                    counts[s[l]] -= 1
                    c = max(counts.values())
                    l += 1
            r += 1
            

        return max_count
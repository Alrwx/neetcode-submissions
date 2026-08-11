class Solution:

    def encode(self, strs: List[str]) -> str:
        # length, delim, word

        out = ""

        for ele in strs:
            out += str(len(ele)) + "_" + ele 

        return out

    def decode(self, s: str) -> List[str]:
        #two pointer, i to the beginning, j to the delimeter
        delim = "_"
        res = []
        i = 0

        #making sure the first pointer is good
        while i < len(s):
            j = i
            while s[j] != delim:
                #we want j to be at the delim
                j += 1

            length = int(s[i:j])

            #char after the delim
            i = j + 1
            res.append(s[i:i+length])

            #length char after the delmi
            i += length
        return res


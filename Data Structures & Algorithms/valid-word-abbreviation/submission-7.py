class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #numbers cannot be consecutive, i.e 97 is treated as 97 and not 9,7
        # can end in a number
        #no leading zeros

        #approach ideas
        #iterate through abbrev list, see if the respective index matches

        #when come across a number, get the WHOLE number (while loop)
        #check if there are enough letters to fit that number

        #then resume

        if len(abbr) > len(word):
            return False

        #iterate through the abbreviation
        aindex = 0
        windex = 0

        while aindex < len(abbr):
            if windex > len(word)-1:
                return False

            #if the abbr char is not a letter
            print(aindex)
            if abbr[aindex].isnumeric():
                sstr = ""
                if abbr[aindex] == "0":
                    return False
                while aindex + 1 <= len(abbr) and abbr[aindex].isnumeric():
                    sstr += abbr[aindex]
                    aindex+=1
                num = int(sstr)
                if windex + num > len(word):
                    print("wrong indx", aindex, windex)
                    return False
                windex += num

            else:
                if abbr[aindex] == word[windex]:
                    aindex +=1
                    windex += 1
                    continue
                return False
        return True



class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.length() - 1;

        // std::string let = "abcdefghjklmnopqrstuvwxyz1234567890";

        while (l < r) {
            while (l < r && !isNum(s[l]) && !isAlpha(s[l])) {
                l++;
            }
            while (r > l && (!isAlpha(s[r]) && !isNum(s[r]))) {
                r--;
            }
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    bool isAlpha(char s) {
        if ((s >= 'a' && s <= 'z')  || (s >= 'A' && s <= 'Z')) {
            return true;
        }
        return false;
    }

    bool isNum(char s) {
        if (s >= '0' and s <= '9') {
            return true;
        }
        return false;
    }
};

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;

        while (start <= end) {
            int ind = start + ((end - start) / 2);

            if (nums[ind] < target) {
                start = ind + 1;
            }

            else if (nums [ind] > target) {
                end = ind - 1;
            }

            else if (nums[ind] == target) {
                return ind;
            }
        }
        return -1;
    }
};

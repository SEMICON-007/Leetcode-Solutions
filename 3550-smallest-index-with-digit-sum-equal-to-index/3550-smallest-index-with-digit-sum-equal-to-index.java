
class Solution {
    public int smallestIndex(int[] nums) {

        int n = nums.length;
        int digitSum = 0;

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            digitSum = 0;

            while (num > 0) {
                int digit = num % 10;
                digitSum += digit;
                num /= 10;
            }

            if (digitSum == i) {
                return i;
            }
        }

        return -1;
    }

}
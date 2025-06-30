class Solution {
    public void sortColors(int[] nums) {
        int l = 0, m = 0, h = nums.length - 1;

        while (m <= h){
            if(nums[m] == 0) {
                int temp = nums[l];
                nums[l++] = nums[m];
                nums[m++] = temp;
            }
            else if(nums[m] == 2) {
                int temp = nums[h];
                nums[h--] = nums[m];
                nums[m] = temp;
            } else {
                m++;
            }
        }
    }
}
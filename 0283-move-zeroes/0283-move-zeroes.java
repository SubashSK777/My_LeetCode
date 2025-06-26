class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0;
	
	int size = nums.length;

	for (int j = 0; j < size; j++){
		if(nums[j] != 0) {
			int temp = nums[i];
			nums[i] = nums[j];
			nums[j] = temp;
			i++;
		}
	}
    }
}
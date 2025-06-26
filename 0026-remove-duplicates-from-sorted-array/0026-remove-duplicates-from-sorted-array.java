class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;

	int size = nums.length;

	for(int j = 1; j < size; j++){
		if (nums[i] != nums[j]){
            i++;
			nums[i] = nums[j];
			
		}
	}
	return i + 1;
    }
}
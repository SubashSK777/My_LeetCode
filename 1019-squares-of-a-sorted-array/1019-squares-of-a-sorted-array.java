class Solution {
    public int[] sortedSquares(int[] nums) {
	int marker = nums.length - 1, start = 0, end = nums.length - 1;

	int[] res = new int[nums.length];

	while (start <= end) {
		int beg = nums[start] * nums[start];
		int fin = nums[end] * nums[end];

		if (beg > fin) {
			res[marker] = beg;
			marker--;
			start++;
		} else {
			res[marker] = fin;
			marker--;
			end--;
		}
	}
	return res;
    }
}
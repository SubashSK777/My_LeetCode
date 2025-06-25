class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int maxSum = 0, winSum = 0;

        for(int i = 0; i < k; i++){
            maxSum += nums[i];
        }

        winSum = maxSum;

        for(int i = k; i < nums.length; i++){
            winSum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, winSum);
        }

        double res = maxSum / (double) k;
        return res;
    }
}
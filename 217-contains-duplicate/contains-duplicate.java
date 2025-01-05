class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet res = new HashSet<>();
        for (int i : nums) {
            if (res.contains(i)){
                return true;
            } else {
                res.add(i);
            }
        } return false;
    }
}
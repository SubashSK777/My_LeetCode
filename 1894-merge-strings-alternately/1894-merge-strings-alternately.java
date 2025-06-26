class Solution {
    public String mergeAlternately(String word1, String word2) {
        int i = 0, j = 0;

        int l_w1 = word1.length();

        int l_w2 = word2.length();

        Scanner sc = new Scanner(System.in);

        StringBuilder sb = new StringBuilder();

        while (i < l_w1 || j < l_w2) {

            if (i < l_w1) {
                sb.append(word1.charAt(i));
                i++;
            }

            if (j < l_w2) {
                sb.append(word2.charAt(j));
                j++;
            }

        }
        return sb.toString();

    }
}
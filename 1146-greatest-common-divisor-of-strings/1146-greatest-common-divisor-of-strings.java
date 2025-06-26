class Solution {
    public String gcdOfStrings(String str1, String str2) {
        
	if(!(str1 + str2).equals(str2 + str1)) return "";

	int a = str1.length();
	int b = str2.length();

	int Str_gcd = gcd(a, b);

	return str1.substring(0, Str_gcd);
    }

        private int gcd(int a, int b) {
            if (b == 0) return a;
            else return gcd(b, a % b);
        }
    
}

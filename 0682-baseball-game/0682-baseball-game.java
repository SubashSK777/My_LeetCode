class Solution {
    public int calPoints(String[] operations) {
        int res = 0;
        Stack<Integer> stack = new Stack<>();

        for (String s : operations) {
            if (s.equals("C")) {
                stack.pop();
            }
            else if (s.equals("D")) {
                int d = stack.peek();
                stack.push(d * 2);
            }
            else if (s.equals("+")) {
                int popp = stack.pop();
                int d = stack.peek();
                stack.push(popp);
                stack.push(popp + d);
            }
            else {
                int num = Integer.parseInt(s);
                stack.push(num);
            }
        }
        int sum = 0;

        for (int i : stack) {
            sum += i;
        }
        return sum;

    }
}
class Solution {
    public int calPoints(String[] ops) {
        Stack <Integer> stack = new Stack<>();

        for(String c : ops) {
            if (c.equals("C")){
                stack.pop();
            } else if (c.equals("D")) {
                int popp = stack.peek();
                stack.push(popp * 2);
            } else if (c.equals("+")) {
                int popp = stack.pop();
                int peak = stack.peek();
                stack.push(popp);
                stack.push(popp + peak);

            } else {
                int num = Integer.parseInt(c);
                stack.push(num);
            }

        }
        int sum = 0;
        for (int n : stack){
            sum += n;
        }
        return sum;
    }
}
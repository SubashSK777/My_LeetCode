class Solution {
    public String removeDuplicates(String s) {
        Stack <Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if(stack.isEmpty()) {
                stack.push(c);
            } else if (stack.peek().equals(c)) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        return sb.toString();
    }
}
class Solution {
    public String simplifyPath(String path) {
        String[] arr = path.split("/");
        Stack<String> stack = new Stack<>();
        for (String c : arr) {
            if (c.equals(".") || c.equals("")) {
                continue;
            } else if (c.equals("..")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
                
            } else {
                stack.push(c);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (String s : stack) {
            sb.append("/").append(s);
        }
        return sb.length() == 0 ? "/" : sb.toString();
    }
}
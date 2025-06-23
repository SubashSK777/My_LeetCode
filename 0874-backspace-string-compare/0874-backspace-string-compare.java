class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> s_stack = new Stack<>();
        Stack<Character> t_stack = new Stack<>();

        for (char c : s.toCharArray()) {
                if(s_stack.isEmpty() && c == '#') {
                    continue;
                } else if (!s_stack.isEmpty() && c == '#'){
                    s_stack.pop();
                } else {
                    s_stack.push(c);
                }
        }
        for (char c : t.toCharArray()) {
                if(t_stack.isEmpty() && c == '#') {
                    continue;
                } else if (!t_stack.isEmpty() && c == '#'){
                    t_stack.pop();
                } else {
                    t_stack.push(c);
                }
        }
        return t_stack.equals(s_stack);
        
    }
}
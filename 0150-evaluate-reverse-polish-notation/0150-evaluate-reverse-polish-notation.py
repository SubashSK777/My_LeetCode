class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val in {'+', "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if val == "+":
                    result = a + b 
                
                elif val == "-":
                    result = a - b

                elif val == "*":
                    result = a * b
                
                else:
                    result = int(a / b)

                stack.append(result)

            else:
                stack.append(int(val))

        return stack[0]

            
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "-":
                b = stack.pop()
                a = stack.pop()
                c = a - b
                stack.append(c)
            elif c == "+":
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(c)

            elif c == "*":
                b = stack.pop()
                a = stack.pop()
                c = a * b
                stack.append(c)
            
            elif c == "/":
                b = stack.pop()
                a = stack.pop()
                c = a / b
                stack.append(int(c))
            else:
                stack.append(int(c))
        return stack.pop()
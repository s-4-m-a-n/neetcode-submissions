class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "-+/*"
        for c in tokens:
            if c in ops:
                b = stack.pop()
                a = stack.pop()
                if c == "-":
                    c = a - b
                elif c == "+":
                    c = a + b
                elif c == "*":
                    c = a * b               
                elif c == "/":
                    c = a / b
            stack.append(int(c))
        return stack.pop()
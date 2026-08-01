
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y if y else 0

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val_stack = []
        operators = {"+": add, 
                     "-": sub,
                     "*": mul, 
                     "/": div}

        for x in tokens:
            if x in operators:
                num2 = val_stack.pop()
                num1 = val_stack.pop()
                res = operators[x](num1,num2)
                val_stack.append(int(res))
            else:
                val_stack.append(int(x))
        return val_stack[-1]
             
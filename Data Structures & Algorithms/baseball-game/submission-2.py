class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] # as a stack
        total = 0 
        for op in operations:
            if op == "+":
                prev_sum = record[-1]+record[-2]
                record.append(prev_sum)
                total += prev_sum
            elif op == "D":
                prev_double = 2*record[-1]
                record.append(prev_double)
                total += prev_double
            elif op == "C":
                total -= record.pop()
            else:
                record.append(int(op))
                total += int(op)
        return total
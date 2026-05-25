class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [0] * len(operations)
        pointer = 0
        total = 0 
        for op in operations:
            if op == "+":
                prev_sum = record[pointer-1]+record[pointer-2]
                record[pointer] = prev_sum
                pointer += 1
                total += prev_sum
            elif op == "D":
                prev_double = 2*record[pointer-1]
                record[pointer] = prev_double
                pointer += 1
                total += prev_double
            elif op == "C":
                pointer -= 1
                total -= record[pointer]
            else:
                record[pointer] = int(op)
                pointer += 1
                total += int(op)
        return total
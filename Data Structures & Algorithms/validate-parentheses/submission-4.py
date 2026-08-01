class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sym_mapper = {
            "[": "]",
            "(": ")",
            "{": "}"
        }

        for c in s:            
            if c in sym_mapper.values():
                if len(stack) > 0 and sym_mapper[stack[-1]] == c:
                    stack.pop()           
                else:
                    return False
            else:
                stack.append(c)
            
        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {"(", "{", "["}
        for c in s:
            if c in opening:
                stack.append(c)
            elif len(stack) > 0:
                top_c = stack.pop()
                if top_c == "(" and c != ")":
                    return False
                elif top_c == "{" and c != "}":
                    return False
                elif top_c == "[" and c != "]":
                    return False
            else:
                return False
                
        return len(stack) == 0
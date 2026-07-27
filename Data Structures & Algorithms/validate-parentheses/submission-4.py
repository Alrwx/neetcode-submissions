class Solution:
    def isValid(self, s: str) -> bool:
        val = "([{"
        stack = []

        for a in s:
            if a in val:
                stack.append(a)
            else:
                if not stack:
                    return False

                if a == ")":
                    if stack.pop() != "(":
                        return False
                elif a == "]":
                    if stack.pop() != "[":
                        return False
                else:
                    if stack.pop() != "{":
                        return False
        return len(stack) == 0
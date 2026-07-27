class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"

        for i in range(len(tokens)):
            stack.append(tokens[i])
            # print(stack)
            if tokens[i] in operators:
                # print(stack)
                op = stack.pop()
                # print(stack)
                val2 = int(stack.pop())
                # print(stack)
                # print(val2)
                val1 = int(stack.pop())
                

                if op == "+":
                    stack.append(val1 + val2)
                elif op == "-":
                    stack.append(val1 - val2)
                elif op == "*":
                    stack.append(val1 * val2)
                else:
                    stack.append(val1 / val2)

        return int(stack[0]);
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # when its a number, we want to add it to the stack
        # when its an operator, we perform the operator to the next
        # 2 elements of the stack

        stack = []
        operators = {'+','-','*','/'}

        ans = 0

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                # print(stack)
                if stack:
                    num1 = stack.pop()
                else:
                    num1 = 0
                
                if stack:
                    num2 = stack.pop()
                else:
                    num2 = 0

                if tokens[i] == "+":
                    # print(num1 + num2)
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    # print(num1 - num2)
                    stack.append(num2 - num1)
                elif tokens[i] == "*":
                    # print(num1 * num2)
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
        return stack.pop()
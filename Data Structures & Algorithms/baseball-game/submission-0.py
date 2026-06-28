class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = list()

        for i in operations:
            if i == "+":
                operand_2 = int(stack[-1])
                operand_1 = int(stack[-2])
                result = operand_1 + operand_2
                stack.append(result)
            elif i == "D":
                stack.append(int(stack[-1])*2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
            
        return sum(stack)
        
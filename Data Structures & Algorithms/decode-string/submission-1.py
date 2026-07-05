class Solution:
    def decodeString(self, s: str) -> str:
        stack_1 = []
        stack_2 = []
        num = 0

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
                
            elif char.isalpha():
                stack_1.append(char)

            elif char == "[":
                stack_1.append(char)
                stack_2.append(num)
                num = 0
                
            elif char == "]":
                if stack_2:
                    num = stack_2.pop()
                else:
                    num = 1
                
                dummy = ""
                while stack_1 and stack_1[-1] != "[":
                    dummy = stack_1.pop() + dummy
                stack_1.pop()
                
                print(f"dummy = {dummy}, num = {num}")
                result = dummy * num

                stack_1.append(result)
                num = 0

        return "".join(stack_1)
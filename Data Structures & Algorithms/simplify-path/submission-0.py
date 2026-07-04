class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()

        for char in path.split("/"):
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "/"+"/".join(stack)
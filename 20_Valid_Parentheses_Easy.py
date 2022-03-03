# Use Stack data structure to solve this problem
# Hashmap:
# ) -> (, } -> {, ]->[

# Possibile condition
# () True
# )( False
# ()[]{} True
# ([)] False

class Solution:

    def isValid(self, s:str) -> bool:

        # Stack = empty list
        stack = []
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in closeToOpen:
                # 2. If we got close parenthese, we check whether matching parentheses inside stack 
                # if there is, we pop the stack and remove that last item

                # example s = "()": [] -> [(] -> [()] -> [] 
                # example s = "[{}]()": [] -> [[] -> [[{] -> [[{}] -> [[] -> [[]] -> [] -> [(] -> [()] -> []
                # example s = "{)": [] -> [{] -> [{)] -> False

                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: # 1. Got open parentheses, add to stack
                stack.append(c)

        return True if not stack else False
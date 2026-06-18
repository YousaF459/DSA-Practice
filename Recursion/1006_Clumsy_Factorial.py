class Solution:
    def clumsy(self, n: int) -> int:
        stack = []

        def solve(x, op):
            if x == 0:
                return

            if op == 0:  # *
                if stack:
                    stack[-1] *= x
                else:
                    stack.append(x)
                    op=op-1

            elif op == 1:  # /
                top = stack[-1]
                stack[-1] = int(top / x)

            elif op == 2:  # +
                stack.append(x)

            elif op == 3:  # -
                stack.append(-x)

            solve(x - 1, (op + 1) % 4)

        if n == 1:
            return 1
            
        solve(n, 0)
        return sum(stack)

sol=Solution()
n = 10
print(sol.clumsy(n))
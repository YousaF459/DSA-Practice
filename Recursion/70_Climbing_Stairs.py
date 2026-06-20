class Solution:
    def climbStairs(self, n: int) -> int:
        
        # APPROACH 1: Forward (0 → n) - Your original thinking
        def bt(current, target):
            if current == target:
                return 1
            if current > target:
                return 0
            return bt(current + 1, target) + bt(current + 2, target)
        
        # APPROACH 2: Backward with Memoization (n → 0)
        def btr(current, target, memo=None):
            if memo is None:
                memo = {}
            
            if current == target:
                return 1
            if current < target:
                return 0
            
            if current in memo:
                return memo[current]
            
            memo[current] = btr(current - 1, target, memo) + btr(current - 2, target, memo)
            return memo[current]
        
       
        return btr(5,0)


# Test
sol = Solution()
print(sol.climbStairs(2))  # 2
print(sol.climbStairs(3))  # 3
print(sol.climbStairs(5))  # 8
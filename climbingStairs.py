# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
# 1 <= n <= 45

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.howManyWays(2)
    
    def howManyWays(self, n, memo = {}):
        if n in memo: return memo[n]
        if n == 0: return 1

        ways = 0
        if n >= 1:
            ways = ways + self.howManyWays(n-1, memo)
        if n >= 2:
            ways = ways + self.howManyWays(n-2, memo)
        
        memo[n] = ways
        return ways
    
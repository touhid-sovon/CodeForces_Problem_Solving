class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0
        sub = 1
        while x > 0 and sub <= x:
            x = x - sub
            count += 1
            sub += 2
        return count

sol = Solution()
print(sol.mySqrt(24))

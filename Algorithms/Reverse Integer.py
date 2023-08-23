class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        reversed_num = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            pop = x % 10
            x //= 10
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and pop > 7):
                return 0
            reversed_num = reversed_num * 10 + pop

        return sign * reversed_num

# Test cases
solution = Solution()
print(solution.reverse(123))   # Output: 321
print(solution.reverse(-123))  # Output: -321
print(solution.reverse(120))   # Output: 21

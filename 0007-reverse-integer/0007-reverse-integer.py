class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)
        ans = 0

        while x != 0:
            digit = x % 10
            ans = ans * 10 + digit
            x = x // 10

        ans = sign * ans

        if ans < -2147483648 or ans > 2147483647:
            return 0

        return ans
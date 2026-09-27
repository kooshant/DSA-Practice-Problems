class Solution:
    def fib(self, n: int) -> int:
        previous = 0
        current = 1

        for i in range(n):
            previous,current = current,previous + current
        return previous
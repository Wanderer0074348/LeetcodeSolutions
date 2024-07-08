class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n+1):
            count += k
            count %= i
        return count + 1

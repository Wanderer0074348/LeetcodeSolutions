class Solution:
    def minOperations(self, logs: list[str]) -> int:
        count = 0
        for log in logs:
            if log == '../':
                count = max(0, count - 1) #ensuring the count is not negative
            elif log != './':
                count += 1
        return count



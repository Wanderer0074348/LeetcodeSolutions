class Solution:
    def minOperations(self, logs: list[str]) -> int:
        count = 0
        for log in logs:
            if log == '../':
                count = max(0, count - 1) #ensuring the count is not negative
            elif log != './':
                count += 1
        return count

a = Solution()
print(a.minOperations(["d1/","d2/","../","d21/","./"])) # 2
print(a.minOperations(["d1/","d2/","./","d3/","../","d31/"])) # 3
print(a.minOperations(["d1/","../","../","../"])) # 0

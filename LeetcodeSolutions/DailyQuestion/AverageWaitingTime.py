class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        time = 0
        wait = 0
        for c in customers:
            if time < c[0]:
                time = c[0]
            time += c[1]
            wait += time - c[0]
        return wait / len(customers)

a = Solution()
print(a.averageWaitingTime([[1,2],[2,5],[4,3]]))
print(a.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))

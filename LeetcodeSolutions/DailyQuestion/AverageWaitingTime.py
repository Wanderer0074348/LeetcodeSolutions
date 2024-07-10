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


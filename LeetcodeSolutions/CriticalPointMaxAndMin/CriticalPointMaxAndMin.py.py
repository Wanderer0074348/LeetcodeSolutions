class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head:ListNode) -> list[int]:
        nodes = []
        minima = -1
        maxima = -1
        while head:
            nodes.append(head.val)
            head = head.next
        if len(nodes)<3:
            return [minima,maxima]
        critical_points = self.findCriticalPoints(nodes)
        if len(critical_points) < 2:
            return [-1, -1]
        minima = float('inf')  # Initialize minima with infinity
        for i in range(1, len(critical_points)):
            distance = critical_points[i] - critical_points[i-1]
            minima = min(minima, distance)
        maxima = critical_points[-1] - critical_points[0]
        return [minima, maxima]

    def findCriticalPoints(self,nodes):
        critical_points = []
        for i in range(1, len(nodes)-1):
            if nodes[i-1] > nodes[i] and nodes[i+1] > nodes[i]:
                critical_points.append(i)
            elif nodes[i-1] < nodes[i] and nodes[i+1] < nodes[i]:
                critical_points.append(i)
        return critical_points
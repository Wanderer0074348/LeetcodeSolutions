class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrank = numBottles
        while numBottles >= numExchange:
            exchanged = numBottles // numExchange
            leftovers = numBottles % numExchange
            totalDrank += exchanged
            numBottles = exchanged + leftovers
        return totalDrank

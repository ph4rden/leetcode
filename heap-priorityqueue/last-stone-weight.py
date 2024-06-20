import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since heapq in python utilizes a min-max heap, we're going to store the negation of the values so that
        # it can act as a max-min heap instead
        self.heap = [-stone for stone in stones]
        heapq.heapify(self.heap)

        while len(self.heap) > 1: 
            y = -heapq.heappop(self.heap)
            x = -heapq.heappop(self.heap)
            # if x == y: 
            #   no need to do this bc we're already popping both stones
            if x != y: 
                # 2 heaviest stones are already popped so now we're just updating y and adding it back
                temp = y - x 
                heapq.heappush(self.heap, -temp)
        
        if self.heap: 
            return -self.heap[0]
        else:
            return 0

if __name__ == "__main__":
    # Example usage
    stones = [2, 7, 4, 1, 8, 1]
    solution = Solution()
    result = solution.lastStoneWeight(stones)
    print(f"The last stone weight is: {result}")
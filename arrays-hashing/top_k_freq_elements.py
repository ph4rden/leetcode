from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # print(count)
        heap = [(c, n) for (n, c) in count.items()]
        # print(heap)
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [n for (c, n) in heap]

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)
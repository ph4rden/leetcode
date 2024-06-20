import heapq

class KthLargest(object): 
    
    def __init__(self, k, nums): 
        # defining value in instance of the class
        self.k = k
        self.heap = nums
        
        # use heapify to turn nums into a min-max heap 
        heapq.heapify(self.heap)

        # ensure heap only holds k amount of values cause we only want the Kth largest value
        while len(self.heap) > self.k: 
            heapq.heappop(self.heap)
        
        
    def add(self, val): 
        # add val to heap
        heapq.heappush(self.heap, val)
        
        # only need to pop once because __init__ takes care of the intial size of nums to the size we want
        if self.heap > self.k: 
            heapq.heappop(self.heap)
        
        # return the min val in our heap which should be the Kth largest value.
        return self.heap[0]
    
if __name__ == "__main__": 
    # Example usage:
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  # Output: 4
    print(kthLargest.add(5))  # Output: 5
    print(kthLargest.add(10)) # Output: 5
    print(kthLargest.add(9))  # Output: 8
    print(kthLargest.add(4))  # Output: 8
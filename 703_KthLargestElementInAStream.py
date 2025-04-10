'''
===703. Kth Largest Element in a stream===

Write a class with a constructor that initializes an object 
    that contains a stream of values and returns the kth largest
    value whenever a new value is added

-Observations:
    * Brute force:
        Sort on initialization: O(nlogn)
        Insert on add, return kth largest element: logn + n
    * Max heap:
        Initialize max heap on initialization: O(nlogn)
        Pop k-1 elements, store kth, insert back into the heap, return kth element: O(klogn)
        Better: store two max heaps, one for reference/adding, one for popping
            Copy the reference heap into the adding heap after every add

'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        self.nums = nums
        print(self.nums)

    def add(self, val: int) -> int:
        print(self.nums)
        heapq.heappush(self.nums, val*-1)
        kthLargestHeap = self.nums.copy()
        for i in range(self.k - 1):
            heapq.heappop(kthLargestHeap)
        return heapq.heappop(kthLargestHeap) * -1

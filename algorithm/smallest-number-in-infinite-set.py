import heapq


# tag: heap, priority_queue, ordered_set
class SmallestInfiniteSet:
    """
    https://leetcode.com/problems/smallest-number-in-infinite-set/
    - 무한 집합에서 가장 작은 수를 pop하고, 다시 추가하는 문제
    - popSmallest() : 가장 작은 수를 pop하고, 다음 수를 추가
    - addBack(num) : num을 다시 추가 but heap에 있는 수는 제외
    """

    def __init__(self):
        self.min_heap = [i for i in range(1, 1001)]  # Initialize with some range
        self.added = set(self.min_heap)  # Track added numbers dup num check
        heapq.heapify(self.min_heap)  ## heap자료형 변환
        self.next_min = 1001  # Next minimum number to add if needed

    def popSmallest(self):
        smallest = heapq.heappop(self.min_heap)
        self.added.remove(smallest)
        if self.next_min not in self.added:
            heapq.heappush(self.min_heap, self.next_min)
            self.added.add(self.next_min)
            self.next_min += 1
        return smallest

    def addBack(self, num):
        if num not in self.added:
            heapq.heappush(self.min_heap, num)
            self.added.add(num)
            if num == self.next_min:
                self.next_min += 1

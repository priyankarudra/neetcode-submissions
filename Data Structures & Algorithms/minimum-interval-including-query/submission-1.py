class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        res = []

        for q in queries:
            cur = -1
            for i in range(len(intervals)):
                if intervals[i][0] <= q and q <= intervals[i][1]:
                    length = intervals[i][1] - intervals[i][0] + 1
                    if cur == -1 or length < cur:
                        cur = length              
            res.append(cur)
        return res
        """

        intervals.sort()
        min_heap = []
        res = {}

        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r-l+1, r))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            res[q] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]





        
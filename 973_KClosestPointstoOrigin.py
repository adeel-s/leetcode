'''
===973. Kth Closest Points to the Origin

-Input
    List[List[int]] points: a list of (x, y) coordinates that represent points on a cartesian plane
        len(points) is between 1 and 1000 
        points[i][0], points[i][1] are between -100 and 100
    int k: the rank of points closest to the origin, (0, 0)
        k is between 1 and 1000

-Output
    List[List[int]] result: the k closest points to the origin

* Observations:
    * Distance form the origin: sqrt(x^2 + y^2)
    * Each point has an associated distance from the origin
    * I can calculate this distance for each point and store it in a list
        Then heapify (min heap) the distance list and return the first k elements
        Runtime: n for calculating distance
            nlogn for heapify
            k for returning the points
            O(nlogn)
        Space: O(n) for storing each of the distances and indicies

-Solution
    Implement a min heap
    Calculate distances of each point, store with an index in a min heap
    Pop the heap k times, add each point to the result array
    return the result array


        
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []
        i = 0
        result = []

        for p in points:
            dist = math.sqrt((p[0] * p[0]) + (p[1] * p[1]))
            distances.append([dist, i])
            i += 1
        heapq.heapify(distances)

        i = 0
        for i in range(k):
            nextPoint = points[heapq.heappop(distances)[1]]
            result.append(nextPoint)

        return result



        
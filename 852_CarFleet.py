'''
===#852 Car Fleet===
-Input:
    int target: the distance all cars need to travel
        Between 1 and 1000
    List[int] position: a list of positions of cars 0-n
        All are unique
        Between 0 and target
        Always less than target
    List[int] speed: a list of speeds of cars 0-n
        Between 1 and 100
    n == len(position) == len(speed), between 1 and 1000

-Output:
    result: the number of fleets the cars will arrive in
        A fleet is a sequence of cars that arrive one after another
        Such that every car is going at least as fast as the car ahead of it

-Complexity:
    O(nlogn) time,
    O(n) space

-Observations:
    * Does sorting help?
        Yes!
    * Proposal:
        result = 1
        Sort position and speed by position
        Calculate ETA for each car
        if ETA[i] > ETA[i-1]:
            result += 1
        * Remember: when the car in front is slower than the car behind, the car behind takes
            it's ETA
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        result = 1
        ETAs = []
        cars = sorted(zip(position, speed))
        for car in cars:
            ETAs.append((target - car[0])/car[1])
        print(ETAs)
        for i in range(len(ETAs) - 1, 0, -1):
            if ETAs[i] < ETAs[i-1]:
                result += 1
            else: 
                ETAs[i-1] = ETAs[i]
        return result


        
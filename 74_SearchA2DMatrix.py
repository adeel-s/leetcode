'''
===74. Search a 2D Matrix===

-Input
    int target: an integer number to search for in matrix
        target is between -10000 and 10000
    List[List[int]] matrix: a 2D matrix in which to search for target
        each row in matrix is sorted in ascending order
        the first element in each row of matrixs is larger than the last element in the previous row.
        len(matrix), m, is between 1 and 100
        len(matrix[i]), n, is between 1 and 100
        matrix[i][j] is between -10000 and 10000
-Output
    bool result: whether target exists in matrix

-Complexity
    O(log(mn)) time
    O(1) space

-Observations
    * This looks like it can be solved using a 2D binary search
    * Checking the first and last elements of each row is key
    * Binary search on the heads and tails of each row, then within the target row as usual

-Solution
    binary search the head and tail of each row:
        find the row that could contain the element: the head is less than, the tail is greater than
    Do a normal binary search of the target row

    top = 0
    bottom = len(matrix)
    mid = (top+bottom)//2

    while top <= bottom:
        if matrix[mid][0] == target:
            return true
        elif matrix[mid][0] > target:
            bottom = mid - 1
            mid = (top+bottom)//2
        else:
            if matrix[mid][-1] < target:
                break
            top = mid + 1
            mid = (top+bottom)//2
    row = mid

    left = 0
    right = len(matrix[row])
    mid = (left+right)//2

    while left <= right:
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] > target:
            right = mid-1
            mid = (left+right)//2
        else:
            left = mid+1
            mid = (left+right)//2

    return False
        
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        mid = (top+bottom)//2

        while top <= bottom:
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bottom = mid - 1
                mid = (top+bottom)//2
            else:
                if matrix[mid][-1] > target:
                    break
                top = mid + 1
                mid = (top+bottom)//2
        row = mid

        left = 0
        right = len(matrix[row]) - 1
        mid = (left+right)//2

        while left <= right:
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid-1
                mid = (left+right)//2
            else:
                left = mid+1
                mid = (left+right)//2

        return False
        
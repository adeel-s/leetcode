# LeetCode Problem Solutions
This repo documents my progress through the NeetCode 150 problem set

## Problem Summaries


### 252. Meeting Rooms
    Sort the list of intervals by start time
    If the end time of one meeting is greater than the start time of another:
        This is a conflict
    If this never happens, there are no conflicts

### 253. Meeting Rooms II
    Split the list of intervals into a list of start times and a list of end times
    Initialize a start and and end pointer to the beginning of each list
    If the next start time is less than the next end time:
        Another meeting will start before one ends
        Increase the number of concurrent meetings
    Otherwise, a meeting will end before the next one starts:
        Decrease the number of concurrent meetings
    Return the max number of concurrent meetings

### 56. Merge Intervals
    Sort intervals by start time
    Overlapping intervals will always be adjacent:
        if the current interval overlaps with the next interval:
            merge the intervals into the next Interval
        otherwise add current interval to result list
    
### 57. Insert Interval
    Create an empty list to return the result of insertion
    Iterate through the list, looking for three cases:
    * Case 1: the newInterval comes before the current interval:
        Insert newInterval into the result list
        append the rest of the intervals
        return the result list
    * Case 2: the current interval comes before the newInterval:
        Insert the current interval into the return list
    * Case 3: newInterval overlaps with current interval:
        absorb current interval into newInterval

### 435. Overlapping Intervals
    Sort intervals by start time
    For each interval:
        If the current interval overlaps with the next one:
            Drop the one that ends later
        Otherwise move to the next interval

### 49. Group Anagrams
    For each string in the list:
        Create a frequency array for the string
        Add it to the dictionary, append the word to the value for that array
    return the values of the dictionary

### 1. Two Sum
    Store numbers:indices in a dictionary
    For each number in nums:
        if its compliment is in the dictionary:
            return its index and the current index

### 242. Valid Anagram
    Create frequency arrays for both strings
    Count letter frequency of s
    Count letter frequency of t
    Compare letter frequencies

### 202. Happy number
    Create a set to track numbers that have already been seen
    While n isn't 1 and isn't in the set
        generate the next number and add it to the set
    return whether n is equal to 1

### 198. House Robber
    Adjacent houses cannot be robbed:
        Store best value of previous elements AND
        best value of previous elements not including the previous element
        For each house:
            take the maximum of: the previous previous best + current value AND
                the previous best value
            previous-previous-best = previous-best
            previous-best = current
        return the previous-best, which is the best possible value by the end of the list

### 150. Reverse Polish Notation
    Store numbers in a stack as operands
    When an operator is encountered, pop two operands and operate
    Each input is gauranteed to be valid
    Handle division by zero and integer division of negatives

### 213. House Robber II
    Now the houses are in a circle, so the first and last houses are adjacent
    If there is only one house, return the value of that house
    Otherwise, return the max of: 
        the houses, skipping the first, and the houses, skipping the last

### 322. Coin Change
    Maintain a list of minimum coins for each possible value of amount
    Base case: minCoins[0] = 0
    For every number up to amount:
        look for a coin of that denomination
            If found, minCoins[i] = 1
            Otherwise, look for minCoins[i - each denomination]
                If found, min(minCoins[i] = minCoins[i - each denomination] + 1)
                Otherwise that amount cannot be made
    return minCoins[amount]
    
### 659. Encode and Decode Strings
    Encode strings by delimiting them using a compound delimiter:
        the length of the next string followed by a special character "#"
    Decode strings by parititioning on each special character, and
        appending the next given length of characters to the output list

### 238. Product of Array Except Self
    Keep track of two products:
        The product of all elements before and after
    Make two passes of the array
        In the first pass, multiply the result array elements
            by the before-product, then update the before product
        In the second pass (backwards), multiply the result array elements
            by the after-product, then update the after product

### 155. Minimum Stack
    Implement init(), push(), pop(), and top() as expected
    For getMin(), an additional stack instance variable is needed to 
        store the state-minimum
        On each push(), the minimum of the incoming value and previous
            minimum is stored as the new minimum
        On each pop(), the most recent minimum is also popped off the
            minimumStack.

### 22. Generate Parentheses
    Create a stack and backtrack:
        If opens == closes == n:
            return the stack of parentheses
        If there are less opens than n:
            Add an open, backtrack, then pop the open
        If there are less closes than opens:
            Add a close, backtrack, then pop the close

### 739. Daily Temperatures
    Create a stack that is monotonically decreasing (or NOT increasing)
    Initialze a result array with len(temperature) 0s
    When adding an element, if the new element is greater than the top of the stack
        pop and update the difference in indices to a result array

### 567. Permutation in String
    Store a frequency array for the string to be found
    Slide a window along the string to check:
    Actually review this problem

### 852. Car Fleet
    After sorting: zip(position, speed), calculate ETAs for each car
    Then, for each car, backwards:
        If the current car's ETA is less than the previous car's
            That means it will "pull ahead", so the number of fleets will increase by one
        Otherwise, the number of fleets will remain the same
            AND the previous car's ETA will become the current car's ETA

### 53. Max Subarray
    Keep track of two variables: sum and best
    Keep a running sum of elements
    Any time the sum goes negative, start over - clean slate
    For each element of the array: 
        add it to the sum
        if sum < 0:
            sum = 0
        Update sum if necessary

### 78. Subsets
    Backtracking: DFS
    At each element, I can add it to the list of possible subsets or not.
    The base case is when I'm recursing on the final element - that's when I add a new
        subset to the result
    Recurse through every element
    If it's the last element, add a copy of the subset to the result and return
    Add the current element and recurse on the next
    remove the current element and recurse on the next

    
### 66. Plus One
    For each digit:
        add the digit and the carry variable
        sum % 10 = new digit value
        sum // 10 = next carry value
    At the end, if the first digit is 0, there must be a carry
        Prepend it to the list

### 15. 3Sum
    For each element, perform the algorithm from Two Sum II:
        Two points, one at each end
        If the sum with nums[i] is greater than 0, decrease right
        Else if the sume is less than 0, increase left
        Else, add to the result array

### 136. Single Number
    Property of the bitwise-XOR operator: commutative
    Since a number XORed with itself is always 0
    And since there are two of each number save for one
    Start with 0, then XOR every element in the list
    Only the unique element will remain

### 5. Longest Palindromic Substring
    For every letter c in s:
        Odd-length palindromes:
        while c has neighbors and they are the same letter
            if the length of this substring is greater than the previous best, update
        Even-length palindromes
        while c plus its right neighbor have neighbors and they are the same letter
            if the length of this substring is greater than the previous best, update
        
### 39. Combination Sum
    DFS(i):
        If the current candidate list sum is equal to target, add a copy to the result list
        For every element from i to the end of the input list:
            Add to the candidate list
            If the sum is less than or equal to the target, recurse
            Pop from the candidate list

### 40. Combination Sum II
    DFS(i): 
        Either add nums[i] to a candidate list or don't:
            If the sum of the candidate list is equal to the target:
                Add a copy to the result list
            If nums[i] is added and the sum of the candidate list is less than target, recurse on i + 1
            If nums[i] is not added:
                skip all elements ahead of nums[i] that are equal to it.

### 191. Number of 1 Bits
    while n is not 0:
        If n is divisible by 2:
            increase the number of 1 bits counter by 1
        Bit-shift n by 2 (dividing it by 2)


### 338. Counting Bits
    Dynamic programming:
        result[0] = 0
        result[1] = 1
        From 2 until n:
            number of bits for result[i] = result[pointer] + 1
            The pointer resets at a power of 2 -

### 55. Jump Game
    Initialize a step variable to 1
    Go backwards through nums, starting at the second to last element:
        if the value of nums[i] is greater than or eqaul to step:
            This means the end can be reached from nums[i]
            Reset step to 1
        else:
            step += 1
    if at the end, step == 1, this means the end can be reached.

### 45. Jump Game II
    Unless all the elements in nums are 1, at some point, I will have a range of elements
        I can jump to. Ex. if nums[0] = 2, I can jump from index 0 to indices 1-2
        nums[1] = 4, nums[2] = 2 → Now I can jump from this range to indicies 3-5
    The number of ranges produced by this traversal equals the number of required jumps

### 134. Gas Station
    If the total cost to complete the circuit is greater than the available gas, it is impossible
    For each station:
        Sum the excess gas available1
        If this sum ever goes to 0, restart the sum at the next index
    This will always return the correct index if a solution exists because if there is enough gas
        to complete the circuit, the starting index can be found iteratively

### 190. Reverse Bits
    For each bit in n:
        Isolate and & with 1
        Add to shift by bit place and add to result

### 647. Palindromic Substrings
    For each letter in s:
        while its neighbors are equal:
            increment result
        repeat for cases where the palindrome root is two letters:
            if current letter and next letter are equal
                while their neighbors are equal:
                    increment result

### 46. Permutations
    Write on 3/23/2025

### 152. Maximum Product Subarray
    Write on 3/23/2025
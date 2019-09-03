All problem statements can be found at:
https://www.hackerrank.com/interview/interview-preparation-kit/warmup/challenges


# Approaches:

## Problem 1: Sock Merchant
The problem revolves around finding the count of unique entities in an array of repeating entities. 
I maintained two arrays: one for holding the unique values and second to count the corresponding occurances of the unique values. 
Once the master array of repeating entities is traversed, the array that maintains the occurances is integer divided by 2 
and added to a running sum. The result is returned when the occurance array is exhausted.

Problem 2: Counting Valleys
The problem seeks to differ a valley from a mountain. This clause can be easily built by understanding the valley pattern. 
A valley will be registered when the hiker levels off at sea level and had to "climb up" in his last step. 
For the sake of simplicity in computation, I assigned a climb up movement to +1 and a climb down movement to a -1. 
Sea level is assigned 0. So the pattern of a valley can be modeled as a transition to sea level by a movement of "climbing up". 
The same condition has been implemented at the end of the for loop.

Problem 3: Jumping on the clouds
I applied a greedy strategy which encourages a double jump whenever possible. The first condition in the loop checks if a double jump
is possible. If so, the index is updated rightaway. If a double jump is not possible, a single jump is executed. 

Problem 4: Repeated String

This problem has optimal substructure property. This means that the problem can be solved by dividing it into subproblems 
and aggregating the solutions of the subproblems to present the final solution. As a matter of fact, I used recursion to 
achieve the Divide and Conquer strategy. However, I did not build the whole string as the repeating unit of the string 
can be searched for the required letter and then multiplied directly by the full occurances of the unit in the larger string to 
easily get the count. The remaining part of the string is then called in the recursive method to yield the final result. 

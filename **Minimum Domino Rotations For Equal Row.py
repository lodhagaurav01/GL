'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6
'''

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        l = len(A)
 
        val = []
        for j in range(1,7):
            flag = 0
            for i, item in enumerate(A):       
                if A[i] != j and B[i] != j:
                    flag = 1
                    break
                if flag == 1:
                    break
            if flag == 0:
                val.append(j)
                
        # print val
        if not val:
            return -1
        
        mintimes = []     
        for item in val:
            mintimes.append(min(l - A.count(item), l - B.count(item) ))
            
        return min(mintimes)

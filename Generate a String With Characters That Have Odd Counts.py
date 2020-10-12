'''
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

 

Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
Example 3:

Input: n = 7
Output: "holasss"
 

Constraints:

1 <= n <= 500
'''


#soln. <c++>

class Solution {
public:
    string generateTheString(int n) {
        string l="";
        int i;
         if(n%2==0)
         {
             for(i=0;i<n-1;i++)
                 l+="a";
                 l+="b";
             return(l);
         }
        else
            {
             for(i=0;i<n;i++)
                 l+="a";
                return(l);
         }
            
        
    }
};
--------------------------------------------------------------------------------
class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        l=""
        if n==1:
            return "x"
        elif n==2:
            return "xy"
        elif n%2==0:
            for i in range(n-1):
                l+=chr(97)
            l+="y"
            return l
        else:
            for i in range(n):
                l +="a"
            return l
                
            

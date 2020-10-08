/*
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.

*/

//Defanging an IP Address c++ solution

class Solution {
public:
    string defangIPaddr(string address) {
        string g;
        int i;
        for (i=0; i<address.length(); i++)
        {
            if(address[i]=='.')      
            {
                g+="[.]";
                   
            }
            else
            {
               g.push_back(address[i]);
                
            }
        }
     return g;
        
    }
};

//Defanging an IP Address py solution

class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.split(".")
        return "[.]".join(address)
            
        





-------------------------------------------------------
import sys
nums=[4,2,5,3,3,6,-8,-6]
min1=min2=min3=min4=20000000
max1=max2=max3=max4=-20000000

for n in nums:
    if n>=max1:
        max4=max3
        max3=max2
        max2=max1
        max1=n
    elif n >=max2:
        max4=max3
        max3=max2
        max2=n
    elif n>=max3:
        max4=max3
        max3=n
    elif n>=max4:
        max4=n
    if n<=min1:
        min4=min3
        min3=min2
        min2=min1
        min1=n
    elif n<=min2:
        min4=min3
        min3=min2
        min2=n
    elif n<=min3:
        min4=min3
        min3=n
    elif n<=min4:
        min4=n    
print (max(max1*max2*max3*max4 , min1*min2*min3*min4,min1*min2*max1*max2) )       


'''
for three numbers:

nums=[4,2,5,3,3,6]
min1=min2=min3=min4=20000000
max1=max2=max3=max4=-20000000

for n in nums:
    if n>=max1:
        max4=max3
        max3=max2
        max2=max1
        max1=n
    elif n >=max2:
        max4=max3
        max3=max2
        max2=n
    elif n>=max3:
        max4=max3
        max3=n
    elif n>=max4:
        max4=n
    if n<=min1:
        min2=min1
        min1=n
    elif n<=min2:
        min2=n
print (max(max1*max2*max3 , max1*min2*min1) )       


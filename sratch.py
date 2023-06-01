from fractions import *
from decimal import *
import sys
input=[[4, 17, 50],
    [4, 30, 50],
    [4,36,67],
       [4,36,67,69]]
pegs=input[3]

'''
     if len(pegs)>3:
        #we will need to split it into two arrays
        #the first containing the distance from the double to the next peg and the last containing the distance from the half to the peg before
'''
def solution(pegs):
    da=[]
    distance=pegs[-1]-pegs[0]
    print(distance)
    for i in range(len(pegs)-1):
        da.append(pegs[i+1]-pegs[i])
    i=0
    increment=Decimal('0.1')
    while i <distance-1:
        if not (distance-(2*i+i))%2:
            print("distance%2",(distance-(2*i+i)))
            if 2*i+(distance-(2*i+i))/2==da[0] and i+(distance-(2*i+i))/2==da[-1]:
                return([Fraction(float(2*i)).limit_denominator().numerator,Fraction(float(2*i)).limit_denominator().denominator])
        i+=increment
        print("da", da)
    return([-1,-1])


result=solution(pegs)
for i in result:
    print(type(i))
print(result)
print(0.2%2)
print(sys.version_info)

#math in python


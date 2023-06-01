from fractions import *
from decimal import *
from collections import *
import time
input=[[4, 17, 50],
    [4, 30, 50],
    [4,36,67],
       [4,36,67,69],
       [4,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,54],
       [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
       [2,10,12,14,16,19],
       [10,22,25,28,31,37.75],
       [1,4,6],
       [14,18,21,25,28,32]]
def solution(pegs):
    da=[]
    distance = pegs[-1]-pegs[0]
    for i in range(len(pegs) - 1):
        da.append(pegs[i+1] - pegs[i])
    dictionary=OrderedDict()
    summation = 0
    for i in range(len(pegs)):
        if i==0 or i ==len(pegs)-1:
            dictionary.setdefault(pegs[i],[1])
        else:
            dictionary.setdefault(pegs[i],[1,1])
    keys = list(dictionary.keys())
    increment = Decimal('0.1')
    number = 0 + increment
    dictionary_values = list(dictionary.values())

    while summation!=distance and number<da[0]-increment:
        summation = 0
        jump = False
        for k in range(len(dictionary_values)):
            if k==0 or k==len(keys)-1:
                dictionary[keys[0]][0]=number
                dictionary[keys[len(keys)-1]][0]=number/2
            elif k>len(keys)-1:
                print("CAUTION,DANGER!!!")
                exit("Fix code")
                pass
            else:
                replacement=da[k-1]-dictionary[keys[k-1]][0]
                if replacement<=0:
                    jump=True
                dictionary[keys[k]][0]=replacement
                dictionary[keys[k]][1]=replacement
            # print(k)
            # print("Dictionary values:",dictionary_values, dictionary_values[k])

            summation += sum(dictionary_values[k])
        # print("Dictionary",dictionary)
        # print("DA",da)
        # print("Summation",summation)

        if summation==distance and not jump:
            return[int(Fraction(number).limit_denominator().numerator),int(Fraction(number).limit_denominator().denominator)]
        number += increment


    return [-1,-1]











start=time.time()
for i in input:
    result=solution(i)
    print("RESULT",result)
end=time.time()
print(end-start)
from fractions import *
from decimal import *
from collections import *
input=[[4, 17, 50],
    [4, 30, 50],
    [4,36,67],
       [4,36,67,69],
       [4,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,54],
       [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
       [2,10,12,14,16,19],
       [10,22,25,28,31],
       [1,4,6],
       [14,18,21,25,28,32]]
input1=[ [4, 30, 50],
        [1, 5, 10],
     [2, 5, 8, 12],
   [1, 3, 5, 7, 9],
 [4, 7, 9, 12, 15],
[2, 6, 12, 20, 30],
 [1, 5, 9, 14, 20],
[10, 20, 30, 40, 50],
 [1, 3, 7, 15, 31],
 [1, 4, 9, 16, 25]]
pegs=input[1]

def solution(pegs):
    da=[]
    distance = pegs[-1]-pegs[0]
    getcontext().prec = 10
    getcontext().rounding=ROUND_DOWN
    for i in range(len(pegs) - 1):
        da.append(pegs[i+1] - pegs[i])
    dictionary=OrderedDict()
    dictionary[0]=[0]
    summation = 0
    for i in range(len(pegs)):
        if i==0 or i ==len(pegs)-1:
            dictionary.setdefault(pegs[i],[1])
            summation+=1
        else:
            dictionary.setdefault(pegs[i],[1,1])
            summation+=2
    allotted=distance-summation
    keys = list(dictionary.keys())[1:]

    # help as assign the values for the first and last values of the dictionary
    increment = Decimal('0.1')
    number = 0 + increment
    dictionary_values = list(dictionary.values())[1:]
    while summation!=distance and number<da[0]-increment:
        #keep track of where we are in the da and also possibly keep track of where we are in the dictionary i.e., keys
        i=0



        summation = 0
        for k in range(len(dictionary_values)):

            if i==0 or i==len(keys)-1:
                dictionary[keys[0]][0]=number
                dictionary[keys[len(keys)-1]][0]=number/2
            elif i>len(keys)-1:
                pass
            else:

                replacement=da[i-1]-dictionary[keys[i-1]][0]
                if replacement>0:
                    dictionary[keys[i]][0]=replacement;dictionary[keys[i]][1]=replacement
            i+=1
            summation += sum(dictionary_values[k])

        if summation==distance:
            return[int(Fraction(number).limit_denominator().numerator),int(Fraction(number).limit_denominator().denominator)]
        number+=increment
    return[-1,-1]
result=solution(pegs)
print("RESULT",result)

for i in input1:
    result=solution(i)
    print("RESULTER",result)





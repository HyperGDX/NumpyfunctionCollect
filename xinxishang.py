import math
from fractions import Fraction
lists = list(map(str, input().strip().split()))
def convertlists(l):
    sum = 0.0
    for i in l:
        sum += Fraction(i) * math.log2(Fraction(i))
    
    return -sum
print(convertlists(lists))

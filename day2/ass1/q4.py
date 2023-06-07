#q4
import string as s
import random as r

#4.1
string=[0]*100
for i in range(0,100):
    str=r.sample(s.ascii_letters,6)
    string[i]="".join(str)
    print(string[i])

#4.2
def isPrime(n):
    for i in range(2,n//2 + 1):
        if n%i == 0:
            return 0
    return 1

for i in range(600,801):
    if isPrime(i) :
        print(i)
        
#4.3
def isDiv(n):
    if (n%7 == 0) and (n%9 == 0):
        return 1
    return 0

for i in range(100,1001):
    if isDiv(i):
        print(i)

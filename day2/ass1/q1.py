#q1
L=[11,12,13,14]

#1.1
L.append(50)
L.append(60)

#1.2
del L[0]
del L[1]

#1.3
L.sort()

#1.4
L.sort(reverse=True)

#1.5
if (13 in L) == True:
    print("13 found")
else:
    print("13 not found")

#1.6
l=len(L)
print("number of elements in L:",l)

#1.7
print("sum of L is:",sum(L))

#1.8,1.9
even=0
odd=0
for i in range(0,len(L)):
    if (L[i] % 2) == 0:
        even=even+L[i]
    else:
        odd=odd+L[i]
print("sum of even numbers in L:",even)
print("sum of odd numbers in L:",odd)

#1.10
def isPrime(n):
    for i in range(2,n//2 + 1):
        if n%i == 0:
            return 0
    return 1
prime=0
for i in range(0,len(L)):
    if isPrime(L[i]) :
        prime=prime+L[i]
print("sum of prime numbers in L:",prime)

#1.11
print("before clear",L)
L.clear()
print("after clear",L)

#1.12
del L
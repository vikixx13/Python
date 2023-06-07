#q3
S1=set([10,20,30,40,50,60])
S2=set([40,50,60,70,80,90])

#3.1
S1.add(55)
S1.add(66)

#3.2
S1.remove(10)
S1.remove(30)
print(S1)

#3.3
print("is 40 present in S1? ",40 in S1)

#3.4
print("union of S1 and S2:",S1.union(S2))

#3.5
print("intersection of S1 and S2:",S1.intersection(S2))

#3.6
print("difference of S1 and S2:",S1-S2)
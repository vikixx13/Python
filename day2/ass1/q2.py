#q2
D={1:5.6,2:7.8,3:6.6,4:8.7,5:7.7}

#2.1
D[8]=8.8

#2.2
del D[2]

#2.3
print("is key 6 present in D? ",6 in D)

#2.4 
print("num of elements in D:",len(D))

#2.5
print("sum of elements in D:",sum(D.values()))

#2.6
D[3]=7.1

#2.7
D.clear()
print(D)
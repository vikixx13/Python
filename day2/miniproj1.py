#part1

import random as r

Set         = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
SetSize     = 5
ResultList  = set() 
Iterations  = 1000  

for i in range(Iterations):
    num = r.sample(Set,SetSize)
    num.sort()

    if sum(num) == 0:
        ResultList.add(tuple(num))

for r in ResultList:
	print (r)

# Print total sets
print ("\nTotal Sets: ", len(ResultList))

#part2
#add set upper bound=6 and lower bound=3 and use random func to get setsize
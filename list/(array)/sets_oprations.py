
set1 = {7,8,9,0,'hello',6,9,9,9,5}

#len
print(len(set1))

print(set1)

# add 
set1.add(10)
print(set1)

#copy
set1.copy()
print(set1)

#discard
set1.discard(7)
print(set1)

#union
set2 ={4,5,6,1,2,3,4,11,5}
print(set1.union(set2))
print(set2|set1)

# intersection
print(set1.intersection(set2))
print(set2&set1)

# differnce
print(set1.difference(set2))
print(set2-set1)

# symmetric diffrence
print(set1.symmetric_difference(set2))
print(set2^set1)






# clear
set1.clear()
print(set1)
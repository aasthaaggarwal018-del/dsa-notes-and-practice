list=['mango','pineapple','kiwi','orange','grapes']

# 1 len()
print(len(list))

# 2 negative index
print(list[-2])

# 3 append
list.append('watermelon')
print(list)

# 4 extent
list2=[1,2,3]
list.extend(list2)
print(list)

# 5 insert
list.insert(-3,0)
print(list)

# 6 remove
list.remove(0)
print(list)

# 7 pop
list.pop(4)
print(list)

# 8 min and max
print(min(list2))
print(max(list2))

# 9 count
list3=[1,1,1,2,3,4,6,8,8,8,8,8,5,3,4]
print(list3.count(8))

# 10 sort
list3.sort()
print(list3)

# 11 reverse
list.reverse()
print(list)

# 12 copy
list4=list.copy()

list4[2]='banana'
list[-1]=100

print(list4)
print(list)

# 13 index
print(list.index('watermelon'))

if 'papaya' in list:
    print(list.index('papaya'))
else:
    print('not present')

# 14 clear
list.clear()
print(list)

# 15 slicing
list3.sort()
print(list3)
print(list3[::-2])


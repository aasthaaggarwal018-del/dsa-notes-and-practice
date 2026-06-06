list1 = [ 2,3,4,5,6,7,8,1,2,3,4,5,6,78,]
fre = {}

for i in list1:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1

for i in fre:
    print(f'{i} is present {fre[i]} times')

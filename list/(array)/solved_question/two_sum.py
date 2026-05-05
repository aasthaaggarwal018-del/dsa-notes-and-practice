'''sum two number in array to meet target'''

list=[5,7,11,20,24,30,45]
target=41

n=len(list)
i,j=0,n-1

while i<j:
    sum=list[i]+list[j]
    if sum<target:
        i+=1
    elif sum>target:
        j-=1
    else:
        print ([i+1,j+1])
        break
        

        
    
     



   

              
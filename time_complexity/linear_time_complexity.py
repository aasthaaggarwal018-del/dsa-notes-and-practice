# tc=0(n) 

n=10
'''for i in range(n):
    print(i,end=' ')

for i in range(n+100):
    print(i,end=' ')

for i in range(n-100):
    print(i,end=' ')

for i in range(n*100):
    print(i,end=' ')'''

'''# nested loop
for i in range(n):   # it moves like i then j then i and work in this loop give 10
    for j in range(10):
        print(i,j,end='')
'''

# time complexity = O(n+x)
for i in range(n):
    print(i,end=' ')
x=5
for i in range(x):
    print(i,end=' ')


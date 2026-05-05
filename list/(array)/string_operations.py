st = 'aastha'

# 1 len
print(len(st))

# 2 negative index
print(st[-2])

# 3 upper and lower
print(st.upper())
print(st.lower())

# 4 capitalise
print(st.capitalize())

# 5 count
a=st.count('a')
print(a)

# 6 replace
print(st.replace('a','A'))

# 7 slicing
print(st[2:5])
print(st[::-1])

# 8 find and index
st2='my name is aastha'
print(st2.find('aastha'))
print(st2.index('name'))
print(st2.find('pineapple'))

# 9 start with
print(st.startswith('a'))
print(st.startswith('b'))

# 10 end with
print(st.endswith('a'))
print(st.endswith('b'))

# 11 strip
x='      aastha    '
y='------aastha----'
x=x.strip()
y=y.strip('-')
print(x,'\n',y)

# 12 split
print(st2.split())
print(st2.split('a'))



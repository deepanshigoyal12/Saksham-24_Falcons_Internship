# slicing and indexing 

s='poornima '
print(s[0:5])
# forward slicing

print(s[-5:-1])
print(s[-1:-5])
# backward slicing 

b= 'python program'
print(b[: :])
# reverse order
print(b[-1:])

print(b[:-1])

print(b[::-1])  # reverse order 

ans=s[: : -2]
print(ans)

print(b[1:10:-1])  #empty sring 

print(s[::])
print(s[::1])
print(s[::-1])

print(s[::-2]) # -2 bakward ka  gap lekar value dega 

print(b[-5:-12:-1])
print(b[-15:-1])


print(b[3:-4])


l=[10,'string',1000,12.06]
print(l)
print(id(l))
print(type(l))

print(l[2])
print(l[3])

l[1]=999 # value change karne ke liey 

print(l)

print(id(l))

l1=[10,20,30]

print(l1)
print(id(l1))

l2=list(l1)   # for changing list location 

print(l2)
print(id(l2))

ll=[11,12,13,14,15]
print(ll[0 : 3])
print(ll[: 4 :-1])

print(ll[-20:4])

# nested list 

l1=[1,2,3,4,5,[100,200,]]
print(l1)
print(l1[5])


anss=l1[5][1]

print(len(l1))
print(l1.index(3))

# append

l1.append(9087)                     # for single value append 
l1.extend(["one","thw","thre"])     # for multiple value append 
l1.insert(1,'i am string ')         #when we input in mid  
l1.pop()                            # this function do last value remove  
l1.remove('i am string ')           #it only remove specific value 
l1.clear()                          # It remove entire list 
l1.append(10)
l1.append(-100)

print(l1)
print(max(l1))
print(min(l1))
print(sum(l1))

# list sort / sorting

l1.sort()                       # it run in ascending order 
l1.sort(reverse=True)           # it run in decending
print(l1)

lis=[11,12,13,14]
lis.reverse
print(lis)

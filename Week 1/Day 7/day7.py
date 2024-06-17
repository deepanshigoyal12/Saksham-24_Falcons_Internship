# nested for loop 
a=5

for i in range (1,6):     #rows
       print("row is : " ,i)
          for j in range(1,6):    #columns 
       
            print("*",end="")
      
              print("\a")

n=3
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
        print("\n")


n=5
for i in range(1,n+1):
    for j in range(1,n+1):

        asc=ord('A')
        ch=chr(asc+ i-1)
        print(ch,end="")
        print("\n") 


def one():
    print("i am one function")
 
def fun(one):
    a,b,c,d=11,12 ,13,14
    
    return a,b,c,d
    
    print(one)
    one()


def fun(a,b,c):  #parameters
    print(a,b,c)

fun(b=10,a=34,c=34 ) #arguement


# default argue

def fun(a,b,c=45):  #parameters
    print(a,b,c)

fun(b=10,a=34)  #arguement

def funx(*args):
    print(args)
    print(type(args))

    for i in args:
        print(i,end="")



funx(1,2,3,4)
funx(1,2,3,4,5)

#keyword arguement 
def aa(**args):
    # print(args)
    # print(type(args))

    for i,j in aa.items():
        print("key: " ,i, " " ,"value ", j)

aa(name="student" , classs="python" , age="50" , work="software ")    


a=21

def fun():
    
    global a
    a=455804

    print(a)


fun()
print(a)

a=10
def fun():
    b=40
    def inner():

        nonlocal b
        b=98
        print(b)

        inner()
        print(b)

fun()   

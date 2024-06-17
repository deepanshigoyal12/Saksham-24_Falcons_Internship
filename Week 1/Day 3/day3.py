
a='A'
print(a)
print(type(a))
# ascii value
print(ord(a))
print(chr(97))


# string
str='i am string'
print(str)

print(type(str))
print(id(str))
print(len(str))

# methods of the string

s='poornima university'
print(s.capitalize())

# title
print(s.title())

print(s.upper()) # this function do capital string 
print(s.lower())   # this function do lower string 
print(s.isupper())    #it's Output is boolean 
print(s.islower())   # it also have boolean output 
print(s.isalpha()) # it also have boolean output but value only have alphabets 

k='name'
print(k.isalpha())


var='1234556666'
print(var.isdigit())  # it only contains numbers



abc='sh2003'
print(abc.isspace)
x='mahavir'
print(x.count('r'))


print(x)

print(s.find('ni'))

print(s.find("ni",8,len(s)))



# strip

a=" good person "
print(a.lstrip)

print(a.rstrip)

print(a.rstrip('son'))


print(a)

# replace
aa="_ python pro"

ans=a.replace('__','i am')

print(ans)
print(aa)
val=a.replace('__',"//")
print(val)

s1='jaipur'
s2='city'

ans=s1.join(s2)

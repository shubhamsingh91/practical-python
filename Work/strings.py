str = "Hello there ghost!"

print("str[0] = ",str[0] )
print("str[1] = ",str[1] )
print("str[4] = ",str[4] )
print("str[-1] = ",str[-1] )

print(str[:1])

print(str[:5])
print(str[6:])

print(str[-4:])
print(str[:-5])

print(len(str))

print('t' in str)
rep = str*5
print(rep)

str1 = str.replace('ghost', 'Ghost')
print(str1)

str2 = str.lower()
print(str2)

# str2[1]  = "1" # not allowed

import sys
print(sys.getsizeof("hello"))
print(sys.getsizeof(b"hello"))

data = b"hello"
print(data[0])

print(str2)
str2 = str2+ "a"
print(str2)
str2 = "b"
print(str2)

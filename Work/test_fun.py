from funs import foo,bar,x
y = 65
foo()
bar()

print("x = ",y)
print("funs.x = ",x)

import sys
print(sys.path)
print(__name__)
import prog

print("imported prog")

print(sys.argv)
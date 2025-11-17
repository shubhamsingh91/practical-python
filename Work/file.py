
filename = "../Data/test.txt"

f = open("../Data/test.txt",'rt')
print(type(f))
data = f.read()
f.close()

# g = open("../Data/test.txt",'wt')
# g.write("adding stuff in")
# g.close()

with open(filename,'rt') as obj:
    data = obj.read()
    for line in data:
        print(line,end='')

with open("outfile.md",'wt') as file:
    file.write("writing in md")

with open("outfile.md",'rt') as file:
    data = file.read()
    print(data)

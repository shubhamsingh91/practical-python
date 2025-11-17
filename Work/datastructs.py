email = None
import csv

if (email):
    print("email is", email)

s = ('GOOG', 100, 40) # tuple
print(s)
print(type(s))
print(s[1])

s = ('MSFT',560,13)
print(s[1])
w = ()
print(w)
t = (1,)
print(t[0])

stock, price, number = s
print("stock =", stock)
print("price = ", price)
print("number = ", number)

# Dictionaries are mutable
s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}

print(s['name'])
print(s['shares'])
s['name'] = 'MSFT'

print(s)

lst1 = list(s)
print(lst1)
print(lst1[0])

for i in s:
    print(i," = ",s[i])

keys = s.keys()
print(type(keys))
print(keys)

for i in keys:
    print(i)

items = s.items()

for i in items:
    print(i)

print("-----------------------------------")
print("-----------------------------------")

records = []
records.append(('GOOG',145,90.0))
records.append(('MSFT',12,45.0))
records.append(('VOO',56,34.0))

print(records[0])

prices = {}
prices['GOOG'] = 187
prices['MSFT'] = 789

for p in prices:
    print( p, " : ",prices[p])

print("-----------------------------------")
prices = {}

with open("Data/prices.csv") as file:
    rows = csv.reader(file)
    for row in rows:
        print(row)
        if (len(row) != 0):
            prices[row[0]] = float(row[1])
        

for p in prices:
    print("price of ", p, " :", prices[p])

print(prices.get('A',0.0))

tech_stocks = {'IBM','APPL','IBM'} # set
print(tech_stocks)
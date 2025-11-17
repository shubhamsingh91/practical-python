email = None

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

import os

path = os.getcwd()
print(path)

file_name = "Data/portfolio.csv"
name_stock = []
count_stock = []
price_stock = []
total_price = 0

f = open(file_name, 'rt')
next(f)

for line in f:
    lst = line.split(',')
    name_stock.append(lst[0])
    count_stock.append(float(lst[1]))
    price_stock.append(float(lst[2]))

n_stocks = len(name_stock)

for i in range(len(name_stock)):
    total_price+= count_stock[i]*price_stock[i]

print("total_price = ", total_price)
f.close()

import os
import pandas as pd

path = os.getcwd()
print(path)

file_name = "Data/portfolio.csv"
name_stock = []
count_stock = []
price_stock = []
total_price = 0

df = pd.read_csv(file_name)

total_price = (df['shares']*df['price']).sum()
print(total_price)
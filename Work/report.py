# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename):
    'Opens a portfolio file and returns a list of tuples'
    portfolio = []
    with open(filename,'rt') as file:
        next(file) # skipping the header

        rows = csv.reader(file)
        for row in rows:
            s = (row[0],int(row[1]),float(row[2]))
            portfolio.append(s)

    return portfolio

filename = "Data/portfolio.csv"

portfolio = read_portfolio(filename)

total_cost = 0

for name,shares,price in portfolio:
    total_cost+= price*shares

print("total_cost = ",total_cost)


def read_portfolio_dict(filename):
    'Opens a portfolio file and returns a list of dictionary'
    portfolio = []
    with open(filename,'rt') as file:
        next(file) # skipping the header

        rows = csv.reader(file)
        for row in rows:
            portfolio.append({'name': row[0], 'price': float(row[2]), 'shares': int(row[1])})
        
    return portfolio

portfolio_dict = read_portfolio_dict(filename)

total_cost = 0

for d in portfolio_dict:
    total_cost+= d['price']*d['shares']

print("total_cost = ",total_cost)
# pprint(portfolio_dict)

filename = "Data/prices.csv"

def read_prices(filename):
    file = open(filename,'rt')
    rows = csv.reader(file)
    prices = {}

    for row in rows:
        if (len(row)!=0):
            prices[row[0]] = float(row[1])
    
    return prices

prices = read_prices(filename)

# computing total value of the portfolio
current_value = 0

for p in portfolio_dict:
    current_value += p['shares']*prices[p['name']]

print("current_value = ", current_value)
print("loss = ",  total_cost-current_value)



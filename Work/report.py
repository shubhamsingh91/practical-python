# report.py
#
# Exercise 2.4

import csv

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

print(portfolio)
total_cost = 0

for name,shares,price in portfolio:
    total_cost+= price*shares

print("total_cost = ",total_cost)
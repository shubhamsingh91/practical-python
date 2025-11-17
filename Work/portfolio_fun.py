import csv

filename = "Data/portfolio.csv"

def portfolio_cost(file_name):
    'Computes the portfolio cost of a set of stocks from filename'
    total_cost = 0
    try:
        file_obj = open(file_name,'rt')
        next(file_obj)   
        rows = csv.reader(file_obj)
        
        for row in rows:
            t = (row[0],float(row[1]),float(row[2]))
            name, shares, price = t # unpacking a tuple
            total_cost+= shares * price

    except FileNotFoundError:
        print("File-name ", file_name, " not found")
             
    return total_cost

def portfolio_cost_dict(file_name):
    'Computes the portfolio cost of a set of stocks from filename using dictionaries'
    total_cost = 0
    try:
        file_obj = open(file_name,'rt')
        next(file_obj)   
        rows = csv.reader(file_obj)
        
        for row in rows:
            d = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2]),
                'seller': 'Charles Schwab'
            }
            
            total_cost+= d['shares'] * d['price']

    except FileNotFoundError:
        print("File-name ", file_name, " not found")
             
    return total_cost

cost  = portfolio_cost(filename)
print("portfolio cost= ", cost)

cost  = portfolio_cost_dict(filename)
print("portfolio cost= ", cost)

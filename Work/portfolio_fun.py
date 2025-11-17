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

            total_cost+= t[1] * t[2]

    except FileNotFoundError:
        print("File-name ", file_name, " not found")
             
    return total_cost

cost  = portfolio_cost(filename)
print("portfolio cost= ", cost)

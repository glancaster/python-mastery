# run interactively python -i path
import csv


class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self, n):
        self.shares = self.shares - n


def read_portfolio(file):
    data = []
    with open(file) as f:
        rows = csv.reader(f)
        headers = next(rows)     # Skip headers
        for row in rows:
            try : data.append(Stock(str(row[0]),int(row[1]),float(row[2])))
            finally : pass
    return data

def print_portfolio(pf):
    print('%10s %10s %10s' % ('name','shares','price'))
    print('%10s %10s %10s' % ('-'*6,'-'*6,'-'*6))

    for s in pf:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
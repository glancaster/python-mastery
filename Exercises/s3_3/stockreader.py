

import csv


class Stock:
    types = (str,int,float)
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self, n):
        self.shares = self.shares - n
    @classmethod
    def from_row(cls,row):
        values = [func(val) for func,val in zip(cls.types,row)]
        return cls(*values)

def read_portfolio(file,cls):
    data = []
    with open(file) as f:
        rows = csv.reader(f)
        headers = next(rows)     # Skip headers
        for row in rows:
            try : data.append(cls.from_row(row))
            finally : pass
    return data
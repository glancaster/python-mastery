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

def print_table(pf,attrs):
    nattrs = len(attrs)
    print("".join(["%10s" % x for x in attrs]))
    print("".join(["%10s" % x for x in ["-"*9]*nattrs]))

    for s in pf:
        print("".join(["%10s" % t(v) for v,t in zip([getattr(s,at) for at in attrs], [type(getattr(s,at)) for at in attrs])]))




s = Stock('GOOG', 100, 490.1)
print(s.name) #get
# getattr(s,'name')
s.shares=50 #set
# setattr(s,'shares')
print(s.shares)
# del s.shares 
# delattr(s, 'shares')

print(hasattr(s,'name'))
print(hasattr(s,'gains'))


attrs = ['name', 'shares', 'price']
nattrs = len(attrs)

# print("".join(["%10s" % x for x in attrs]))
# print("".join(["%10s" % x for x in ["-"*9]*nattrs]))
# print("".join(["%10s" % t(v) for v,t in zip([getattr(s,at) for at in attrs], [type(getattr(s,at)) for at in attrs])]))

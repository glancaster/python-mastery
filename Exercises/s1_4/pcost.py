
def portfolio_cost(file) -> float:
    sum : int = 0
    with open(file) as f:
        for line in f.readlines():
            row = line.split()
            try:
                sum += int(row[1])*float(row[2])
            except Exception as e:
                print(f"Couldn't parse: {line}Reason: {e}")
    return sum
file ='Data\\portfolio3.dat'
print(portfolio_cost(file))
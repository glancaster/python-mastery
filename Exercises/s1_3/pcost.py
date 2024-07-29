sum : int = 0
with open('Data\\portfolio.dat') as f:
    for line in f.readlines():
        row = line.split()
        sum += int(row[1])*float(row[2])
        print(row)

print(f"{sum=}")
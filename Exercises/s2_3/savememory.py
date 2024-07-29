import tracemalloc
import csv

# METHOD 1

# tracemalloc.start()
# def read_rides_as_dict(filename):
#     '''
#     Read the bus ride data as a list of dictionaries
#     '''
#     records = []
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headings = next(rows)     # Skip headers
#         for row in rows:
#             route = row[0]
#             date = row[1]
#             daytype = row[2]
#             rides = int(row[3])
#             record = {
#                     'route': route,
#                     'date': date,
#                     'daytype': daytype,
#                     'rides': rides,
#                 }
#             records.append(record)
#     return records

# rows = read_rides_as_dict('Data/ctabus.csv')
# rt22 = [ row for row in rows if row['route']=='22']
# print(max(rt22, key=lambda row: row['rides']))
# print(tracemalloc.get_traced_memory())


# METHOD 2

tracemalloc.start()

f = open('Data/ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
rows = (dict(zip(headers,row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
print(max(rt22, key=lambda row: int(row['rides'])))
print(tracemalloc.get_traced_memory()) 

# Much smaller due to generators 
# generators are like list comp. but not stored


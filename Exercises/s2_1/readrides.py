# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records
def read_rides_as_dict(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                    'route': route,
                    'date': date,
                    'daytype': daytype,
                    'rides': rides,
                }
            records.append(record)
    return records
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of classes
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records
from collections import namedtuple
def read_rides_as_namedtuple(filename):
    '''
    Read the bus ride data as a list of namedtuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            Rownt = namedtuple('Rownt', ['route', 'date', 'daytype', 'rides'])
            record = Rownt(route, date, daytype, rides)
            records.append(record)
    return records
# A class with __slots__
class Rowslots:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
def read_rides_as_classslots(filename):
    '''
    Read the bus ride data as a list of classes
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Rowslots(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('Data/ctabus.csv')
    print('Tuples Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.start()
    rows2 = read_rides_as_dict('Data/ctabus.csv')
    print('Dictionaries Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.start()
    rows3 = read_rides_as_class('Data/ctabus.csv')
    print('class Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.start()
    rows4 = read_rides_as_namedtuple('Data/ctabus.csv')
    print('namedtuple Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
    tracemalloc.start()
    rows5 = read_rides_as_classslots('Data/ctabus.csv')
    print('class with slots Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
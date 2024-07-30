import csv

def read_csv_as_dict(filename, coltypes):
    '''
    Read the csv data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)     # Skip headers
        for row in rows:
            record = { name:func(val) for name, func, val in zip(headers, coltypes, row) }
            records.append(record)
    return records
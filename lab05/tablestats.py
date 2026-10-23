def read_rows(lines):
    data = []
    column = None

    for line in lines:
        line = line.strip()
        if not line: continue
        
        values = [value.strip() for value in line.split(',')]

        if column is None:
            column = values
            continue
        if len(values) != len(column): continue
        row = {}
        for i in range(len(column)):
            row[column[i]] = values[i]
        data.append(row)
    return data


def count_types(rows):
    type = {}
    for i in rows:
        if i['тип'] in type:
            type[i['тип']] += 1
        else:
            type[i['тип']] = 1
    return type

def total_minutes(rows, kind):
    sum = 0
    for i in rows:
        if i['тип'] == kind:
            try:
                sum += float(i['минуты'].replace(',', '.'))
            except ValueError:
                continue
    return round(sum, 1)

def to_csv(counts):
    a = 'тип,количество\n'
    for type in sorted(counts):
        a += f'{type},{counts[type]}\n'
    return a
        

#print(to_csv(count_types(read_rows('events-small.csv'))))

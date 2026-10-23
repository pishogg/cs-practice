from tablestats import *

file = input()
with open(file, encoding="utf-8") as table:
    rows = read_rows(table)

print(len(rows), len(count_types(rows)), total_minutes(rows, 'ошибка'))

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(count_types(rows)))
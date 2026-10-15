from tablestats import *

file = input()
print(len(read_rows(file)), len(count_types(read_rows(file))), total_minutes(read_rows(file), 'ошибка'))

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(count_types(read_rows(file))))
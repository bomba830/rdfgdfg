import csv

file = 'africa_data.csv'

with open(file, newline='', encoding="utf-8-sig") as csvfile:
    data = list(csv.reader(csvfile, delimiter='\t'))  

stats = {"mezainiba": 0, "blivums": 0}
count = 0

def printData(el1, el2, el3, size=25):
    print(el1, ' ' * (size - len(el1)), end='')
    print(el2, ' ' * (size - len(el2)), end='')
    print(el3)

for row in data:

    if len(row) < 3:
        continue

    # header
    if "Valsts" in row[0]:
        printData(row[0], row[1], row[2])
        print('-' * 70)
        continue

    valsts = row[0].strip()
    blivums = float(row[1].strip())
    mezainiba = float(row[2].strip())

    stats["mezainiba"] += mezainiba
    stats["blivums"] += blivums
    count += 1

    printData(
        valsts,
        str(blivums),
        str(mezainiba)
    )

print('_' * 70)

printData(
    "Vidējais",
    f"{stats['blivums'] / count:.2f}",
    f"{stats['mezainiba'] / count:.2f}"
)

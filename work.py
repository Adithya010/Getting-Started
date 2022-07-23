# we made a csv file for work in the CSV folder
# understanding how to read in a csv file

from email import header
import csv
print("One way to go about reading a CSV file ")
print()

rows = []

with open("CSV/work.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)

    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

print("The second way to go about the CSV file ")
print()
print("This is the best way and the easiest form of doing so")

rows = []

with open("CSV/work.csv", 'r') as file:
    csvreader = csv.reader(file)

    items = list(csvreader)

for item in items:   # iterating over the list of items
    print(item)


# always copy the relative path of the csv file and then use in the
# with statement such that we get the o/p
# or else we might end up not getting the o/p

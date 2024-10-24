#to read file
import csv

import sys

#to make a table look
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Invalid number of CLA")

try:

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], "r") as file:
            read = csv.reader(file)
            data = list(read)

    except FileNotFoundError:
        sys.exit("File does not exist")

    for line in data:
        print(tabulate(data[1:], headers=line[0:]))
        break

except Exception as e:
    sys.exit(f"Error occured: {e}")



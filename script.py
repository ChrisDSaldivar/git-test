import sys
from os.path import isfile

filename = "data.txt"

if not isfile(filename):
    print(f"{filename} not found")
    sys.exit(1)

data_file = open(filename, "r")
line = data_file.readline().strip()

count = 0
while line != "":
    val = int(line)
    if val > 10:
        count += 1

    line = data_file.readline().strip()

data_file.close()
print(f"There are {count} numbers over 10")

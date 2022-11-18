filename = "data.txt"

data_file = open(filename, "r")
line = data_file.readline().strip()

while line != "":
    val = int(line)
    if val > 10:
        print(val)
        
    line = data_file.readline().strip()

data_file.close()
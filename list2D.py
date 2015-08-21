__author__ = 'Dixit_Patel'



f = open("data.txt")
rows_count, cols_count = f.readline().split()
line_count = 0
list2D = []
while line_count < int(rows_count):
    line = f.readline().strip().strip("\n")
    if len(line) == 0:
        # blank line
        continue
    row = list(line)[0:int(cols_count)]
    print("row", row)
    list2D.append(row)
    line_count += 1
print(list2D)
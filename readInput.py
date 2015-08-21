__author__ = 'Dixit_Patel'


# print("Enter the value of row:")
# r = input()
# print("Enter the value of column:")
# c = input()

f = open("data.txt")
rows,cols = f.readline().split()

m={}
line_number = 0
while line_number < int(rows):
    # for i in range(int(rows)):
    #     print(i)
    line = f.readline().strip().strip("\n")
    # print("line", line)
    m[line_number] = list(line)[0:int(cols)]
    line_number+=1


print(m)
# for i in range(int(r)):
#     for j in range(int(c)):
#         print(m[i][j])

__author__ = 'Dixit_Patel'
import nester
# read = open("conv.txt","+r")
#
# for line in read:
#     if not line.find(":")== -1:
#         (role,line_said) = line.split(":",1)
#         print( role, " : ",line_said)
#
# read.close()
write = open("conv_write.txt","+w")
man = []
other = []
try:
    read = open("conv.txt","+r")
    for line in read:
        try:
            (role,line_said) = line.split(":",1)
            #print( role, " : ",line_said )

            if(role == 'Man said'):
                man.append(line_said)
            elif(role == 'Other Man said'):
                other.append(line_said)
        except ValueError:
            pass#print(line)

    read.close()
except IOError as err:
    #print("no file")
    print("no file" + str(err))

print("Man, : " , man)
print("Other, : " , other)
# print(man, file = write)
# print(other,file = write)

# print("-->"); nester.fun1(man,True)
with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
    #print(nester.fun1(man,True), file=man_file)
    nester.fun1(man, fh=man_file)
    #print(nester.fun1(other,True), file=other_file)
    nester.fun1(other, fh=other_file)


write.close()

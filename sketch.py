__author__ = 'Dixit_Patel'
import os
if os.path.exists("conv.txt"):
    #read = open("conv.txt","+r")
    with open("conv.txt","+r") as read:
        print("inline -> ");print(man,file=read)
        for line in read:
            try:
                (role,line_said) = line.split(":")
                print( role, " : ",line_said )
            except ValueError:
                pass#print(line)
            except IOError as err:
                print("Error: ",str(err))
        #read.close()

else:
    print("no file")
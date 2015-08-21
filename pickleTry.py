__author__ = 'Dixit_Patel'

import pickle
import nester
# with open('mydata.pickle','wb') as mysavedata:
#     pickle.dump([1, 2, 'three'], mysavedata)
#
# with open('mydata.pickle','rb') as myrestoredata:
#     a_list = pickle.load(myrestoredata)
#
# print(a_list)
print('start read')
man = []
other_man = []
try:
    with open('man_data.txt','r') as man_file, open('other_data.txt','r') as other_file:
        for line in man_file:# and line not in ('\n', ' '):
            man.append(line.strip())
        for line in other_file:
            #print('other_man -> ', line)
            other_man.append(line.strip())

except IOError as err:
    print("error while reading" + str(err))

print('end read')

# print(man)
# print('->',other_man)

print('Start pickle write')
try:
    with open('man_data_pickle.txt','wb') as man_file, open('other_data_pickle.txt','wb') as other_file:
        # nester.fun1(man, fh=man_file)
        # nester.fun1(man, fh=other_file)
        pickle.dump(man, man_file)
        pickle.dump(other_man, other_file)
except IOError as err:
    print('Filename:' + str(err))
except pickle.PickleError as peer:
    print('Picking error' + str(peer))
print('end pickle write')

print('Start pickle read')
man_lst = []
other_man_lst = []

try:
    with open('man_data_pickle.txt','rb') as man_pickle, open('other_data_pickle.txt', 'rb') as other_man_pickle:
        pickle.loads(man_lst,man_pickle)
        pickle.loads(other_man_lst,other_man_pickle)
except pickle.PickleError as peer:
    print('excp while reading pickle' + str(peer))

print('end pickle read')
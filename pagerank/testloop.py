__author__ = 'Dixit_Patel'
output = open("testloop.txt", "w+")

from datetime import datetime
# i=0
# dt = datetime.today()
# print(dt.now())
# while True:
#     print('inside')
#     i += 1
#     print('loopvar',i)
#     if i == 400:
#         print('breaking out')
#         break
# print(dt.now())

# words="A "
# if not words[1:]:
#     print('empty')
# print(words[1:])

# M ={}
# for q in M['X']:
#     print('s')

from collections import OrderedDict
import operator
rel_page_rank = {'WT02-B31-85': 2.4365229571731584e-05, 'WT01-B19-118': 2.795123346812606e-05}
rel_page = {'WT27-B26-166': 2.4365229571731584e-05, 'WT02-B15-103': 0.00578648566131052}
for values in rel_page:
    print(round(rel_page[values],20))
    rel_page[values] = round(rel_page[values], 20)
sorted_x = sorted(rel_page.items(), key=lambda x: x[1] ,reverse=True)
print('orderedval => ', sorted_x)
output.write('sorted_page_rank' + str(sorted_x) + '\n')
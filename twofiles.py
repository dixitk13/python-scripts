__author__ = 'Dixit_Patel'
man = []
other = []
with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
    print(man, file=man_file)
    print(other, file=other_file)

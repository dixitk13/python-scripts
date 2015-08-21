__author__ = 'Dixit_Patel'

from genericFunctions import *
import athletemodel
#from athletemodel import *
import yate
import glob

data_files = glob.glob("../data/*.txt")
#print(data_files)
# print(glob.glob0('data','/*.txt'))
# print(glob.glob1('data','/*.txt'))
athletes = athletemodel.put_to_store(data_files)

# impt line - start response
print(yate.start_response())

print(yate.include_header("Home"))
print(yate.header("AthLetA"))
print(yate.para('Select an athlete from list'))
print(yate.start_form("generate_timing_data.py"))
print(type(athletes))
for athlete in athletes:
    print(yate.radio_button("which_athlete",athletes[athlete].name))
# print(yate.radio_button('James','James'))
# print(yate.radio_button('Mikey','Mikey'))
print(yate.end_form())
print(yate.include_footer({"Home": "/index.html"}))
__author__ = 'Dixit_Patel'

from genericFunctions import *
import athletemodel
#from athletemodel import *
import yate
import glob

data_files = glob.glob("data/*.txt")
print(glob.glob0('data','/*.txt'))
print(glob.glob1('data','/*.txt'))
athletes = athletemodel.put_to_store(data_files)
print(yate.header("ATHLetA"))
print(yate.para('Select an athlete from list'))
print(yate.start_form(''))
print(type(athletes))
for athlete in athletes:
    print(yate.radio_button("which_athlete",athletes[athlete].name))
# print(yate.radio_button('James','James'))
# print(yate.radio_button('Mikey','Mikey'))
print(yate.end_form())
print(yate.include_footer({"Home": "/index.html"}))
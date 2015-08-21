__author__ = 'Dixit_Patel'

from genericFunctions import *
from athletelist import *
from athletemodel import *
import yate
import glob
import cgi
import cgitb

cgitb.enable()

form_data = cgi.FieldStorage()
athletes = get_from_store()

#print('formdata -> ',form_data)

athlete_name = form_data['which_athlete'].value
print(yate.start_response())

print(yate.include_header("Timings Page"))
print(yate.header("Timings"))

print(yate.para('Timing data for ' + athlete_name + ' DOB : ' + athletes[athlete_name].dob))
#print('which -> ',athlete_name)

#athlete_timings = athletes[athlete_name]

print(yate.start_form("generate_timing_data.py"))

#print(yate.u_list(athletes[athlete_name]))
print(yate.u_list(athletes[athlete_name].top3))

print(yate.end_form())

print(yate.include_footer({"Home": "/index.html","yet another athlete " : "/cgi-bin/generate_list.py"}))



# print('athletes', athletes)
# athlete = AthleteList(athletes[athlete_name])
# print('top3 - ', athlete.returnTop3)


#print(type(athlete_timings))
#athlete_timings_top3 = athlete_timings

#print(" -- ", athlete_timings)
#for timing in athlete_timings:


# for athlete in athletes:
#     print(yate.radio_button("which_athlete",athletes[athlete].name))

